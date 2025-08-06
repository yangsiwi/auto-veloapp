import time

import allure
import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# 【核心】我们只需要这两个底层模块
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction


# 项目中常用的操作 找到元素点击  找到元素输入  找元素 显示等待 等待 Keywords(driver)
class Keywords:
    # __init__ 只要实例化类就要传一个driver
    def __init__(self, driver):
        self.driver = driver
        # 定义一个默认的超时时间，方便统一管理
        self.timeout = 30
        # 定义轮询周期
        self.poll_frequency = 0.5

    # --- 基础等待方法 ---
    @allure.step("等待元素出现")
    def wait_for_element_to_be_visible(self, locator, timeout=None):
        """
        等待元素在页面上可见。
        :param locator: 元素定位器。
        :param timeout: 可选的超时时间（秒），如果为None，则使用类中定义的默认超时。
        """
        # 如果没有提供特定的超时时间，就使用类属性中定义的默认值
        wait_timeout = timeout if timeout is not None else self.timeout
        try:
            return WebDriverWait(self.driver, wait_timeout, self.poll_frequency).until(
                ec.visibility_of_element_located(locator)
            )
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), f"等待元素 {locator} 可见超时 ({wait_timeout}秒)",
                          allure.attachment_type.PNG)
            # 抛出异常，让调用方知道等待失败
            raise

    # 【新增】等待元素在页面上消失的方法
    @allure.step("等待元素消失")
    def wait_for_element_to_be_invisible(self, locator, timeout=10):
        """
        在指定时间内等待，直到元素从DOM中移除或变为不可见。
        如果元素本来就不存在，此方法会立刻返回True。
        如果元素在超时后依然可见，则抛出TimeoutException。
        """
        try:
            WebDriverWait(self.driver, timeout, self.poll_frequency).until(
                ec.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            # 如果等待超时，说明Toast一直没消失，这是一个问题
            allure.attach(self.driver.get_screenshot_as_png(), f"等待元素 {locator} 消失超时",
                          allure.attachment_type.PNG)
            print(f"警告：等待元素 {locator} 消失超时！")
            return False

    @allure.step("等待元素可被点击")
    def wait_for_element_to_be_clickable(self, locator):
        """
        等待元素可见并且可被点击。用于点击操作前，比单纯等待可见更可靠。
        """
        try:
            return WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                ec.element_to_be_clickable(locator)
            )
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), f"等待元素 {locator} 可点击超时",
                          allure.attachment_type.PNG)
            raise TimeoutException(f"等待元素 {locator} 可点击超时")

    # 显示等待元素 place (xx.id, 'xx')
    @allure.step("显示等待元素")
    def wait_explicit(self, place):
        ele = WebDriverWait(self.driver, 30).until(lambda x: x.find_element(*place))
        return ele

    # --- 核心操作方法 ---
    @allure.step("点击元素")
    def click_element(self, locator):
        """
        先等待元素可被点击，然后再执行点击操作。
        """
        element = self.wait_for_element_to_be_clickable(locator)
        element.click()

    @allure.step("输入文本")
    def input_text(self, locator, text):
        """
        先等待元素可见再输入。
        """
        element = self.wait_for_element_to_be_visible(locator)
        element.send_keys(text)

    @allure.step("清空并输入文本")
    def clear_and_input_text(self, locator, text):
        """
        将清空和输入两个操作合并，非常实用。
        """
        element = self.wait_for_element_to_be_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("获取元素属性")
    def get_element_attribute(self, locator, attribute_name):
        """
        封装获取元素属性的方法，避免在Page层写太多逻辑。
        """
        element = self.wait_for_element_to_be_visible(locator)
        return element.get_attribute(attribute_name)

    @allure.step("隐藏键盘")
    def hide_keyboard(self):
        """
        判断键盘是否显示，如果显示则隐藏。
        """
        if self.driver.is_keyboard_shown:
            self.driver.hide_keyboard()

    # --- 页面滚动方法 ---

    def _get_screen_size(self):
        """内部辅助方法，获取屏幕尺寸。"""
        return self.driver.get_window_size()

    @allure.step("执行一次向上滑动")
    def swipe_up(self, duration_ms=0):
        size = self._get_screen_size()
        width = size['width']
        height = size['height']

        start_x = width // 2
        start_y = int(height * 0.8)
        end_y = int(height * 0.2)

        # ✅ 创建 PointerInput（用 'touch' 不是 'finger'）
        finger = PointerInput(interaction.POINTER_TOUCH, "finger")

        # ✅ 正确方式：创建 ActionBuilder 并传入 pointer_inputs
        actions = ActionBuilder(self.driver, mouse=finger)

        # ✅ 构建动作链
        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(duration_ms / 1000)
        actions.pointer_action.move_to_location(start_x, end_y)
        actions.pointer_action.release()

        # ✅ 执行滑动
        actions.perform()

    @allure.step("执行一次向下滑动")
    def swipe_down(self, duration_ms=0):
        size = self._get_screen_size()
        width = size['width']
        height = size['height']

        start_x = width // 2
        start_y = int(height * 0.2)  # 从页面上方开始
        end_y = int(height * 0.8)  # 滑到页面下方

        # 创建 PointerInput（仍然是 touch 类型）
        finger = PointerInput(interaction.POINTER_TOUCH, "finger")

        # 创建 ActionBuilder
        actions = ActionBuilder(self.driver, mouse=finger)

        # 构建动作链（从上往下滑）
        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(duration_ms / 1000)
        actions.pointer_action.move_to_location(start_x, end_y)
        actions.pointer_action.release()

        # 执行动作
        actions.perform()

    # 【核心新增】向左滑动的方法
    @allure.step("执行一次向左滑动")
    def swipe_left(self, duration_ms=200):
        """
        从屏幕的右侧中心向左侧中心滑动，模拟向左滑动。
        """
        size = self._get_screen_size()
        width = size['width']
        height = size['height']

        # Y轴保持在屏幕垂直中点，确保是水平滑动
        y = int(height * 0.4)  # 选择一个区域，比如40%的高度，正好在图表区域
        # X轴从右向左
        start_x = int(width * 0.8)
        end_x = int(width * 0.2)

        finger = PointerInput(interaction.POINTER_TOUCH, "finger")
        actions = ActionBuilder(self.driver, mouse=finger)

        actions.pointer_action.move_to_location(start_x, y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(duration_ms / 1000)
        actions.pointer_action.move_to_location(end_x, y)
        actions.pointer_action.release()
        actions.perform()

    # 【核心新增】向右滑动的方法
    @allure.step("执行一次向右滑动")
    def swipe_right(self, duration_ms=200):
        """
        从屏幕的左侧中心向右侧中心滑动，模拟向右滑动。
        """
        size = self._get_screen_size()
        width = size['width']
        height = size['height']

        # Y轴保持在屏幕垂直中点
        y = int(height * 0.45)
        # X轴从左向右
        start_x = int(width * 0.2)
        end_x = int(width * 0.8)

        finger = PointerInput(interaction.POINTER_TOUCH, "finger")
        actions = ActionBuilder(self.driver, mouse=finger)

        actions.pointer_action.move_to_location(start_x, y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(duration_ms / 1000)
        actions.pointer_action.move_to_location(end_x, y)
        actions.pointer_action.release()
        actions.perform()

    @allure.step("获取所有匹配元素的列表")
    def find_all_elements(self, locator):
        """
        等待并返回所有匹配定位器的元素列表。
        """
        try:
            # 等待至少有一个元素出现
            WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                ec.presence_of_all_elements_located(locator)
            )
            return self.driver.find_elements(*locator)
        except TimeoutException:
            # 如果一个都找不到，返回一个空列表
            return []

    @allure.step("滚动直到页面底部")
    def scroll_to_very_bottom(self, max_swipes=300):
        """
        持续向上滑动，直到页面无法再滚动（已到达底部），或达到最大滑动次数。
        """
        # 获取滑动前的页面源码
        page_source_before_swipe = self.driver.page_source

        for i in range(max_swipes):
            allure.attach(f"执行第 {i + 1} 次向上滑动...", name="滚动状态")
            self.swipe_up()
            # 短暂等待UI刷新
            # time.sleep(1)

            # 获取滑动后的页面源码
            page_source_after_swipe = self.driver.page_source

            # 如果滑动后源码没有变化，说明已经到底部了
            if page_source_after_swipe == page_source_before_swipe:
                allure.attach("页面源码未变，已到达底部。", name="滚动结束")
                return True  # 表示成功滚动到底部

            # 更新页面源码，为下一次比较做准备
            page_source_before_swipe = page_source_after_swipe

        # 如果循环结束还没到底部，可以根据需要决定是报错还是警告
        pytest.fail(f"在尝试滚动 {max_swipes} 次后，页面仍未到达底部。")
        return None

    # 在指定元素内部进行水平滑动
    @allure.step("在元素 '{locator}' 内部向左或者右水平直线滑动")
    def swipe_element_horizontally(self, locator, direction: str = "left", duration_ms=200):
        """
        找到一个元素，并在其内部执行水平滑动。
        :param duration_ms:
        :param locator: 要滑动的元素。
        :param direction: "left" 或 "right"。
        """
        # 1. 首先，找到这个元素
        element = self.wait_for_element_to_be_visible(locator)

        # 2. 获取元素的位置和大小
        location = element.location
        size = element.size

        # 3. 【核心】基于元素自身的位置和大小，计算滑动的起止点
        # Y坐标永远在元素的垂直中心
        element_center_y = location['y'] + size['height'] // 2

        if direction == "left":
            # 从元素右侧 80% 处滑到左侧 20% 处
            start_x = location['x'] + int(size['width'] * 0.8)
            end_x = location['x'] + int(size['width'] * 0.2)
        elif direction == "right":
            # 从元素左侧 20% 处滑到右侧 80% 处
            start_x = location['x'] + int(size['width'] * 0.2)
            end_x = location['x'] + int(size['width'] * 0.8)
        else:
            raise ValueError("方向参数必须是 'left' 或 'right'")

        # 4. 执行滑动
        finger = PointerInput(interaction.POINTER_TOUCH, "finger")
        actions = ActionBuilder(self.driver, mouse=finger)
        actions.pointer_action.move_to_location(start_x, element_center_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(duration_ms / 1000)
        actions.pointer_action.move_to_location(end_x, element_center_y)
        actions.pointer_action.release()
        actions.perform()

    @allure.step("在元素 '{locator}' 内部向 '{direction}' 带弧度滑动")
    def swipe_element_horizontally_with_arc(self, locator, direction: str = "left", duration_ms=400,
                                            curve_offset=20):
        """
        找到一个元素，并在其内部执行一个带微小弧度的水平滑动，以模拟更真实的用户手势。
        """
        # 1. 找到元素并获取其几何信息
        element = self.wait_for_element_to_be_visible(locator)
        location = element.location
        size = element.size

        # 2. 计算弧线的三个关键点坐标
        element_center_y = location['y'] + size['height'] // 2

        if direction == "left":
            start_x = location['x'] + int(size['width'] * 0.8)
            end_x = location['x'] + int(size['width'] * 0.2)
        elif direction == "right":
            start_x = location['x'] + int(size['width'] * 0.2)
            end_x = location['x'] + int(size['width'] * 0.8)
        else:
            raise ValueError("方向参数必须是 'left' 或 'right'")

        mid_x = (start_x + end_x) // 2
        mid_y_with_offset = element_center_y + curve_offset

        # 3. 严格使用您成功的代码模式来构建和执行手势
        finger = PointerInput(interaction.POINTER_TOUCH, "finger")
        actions = ActionBuilder(self.driver, mouse=finger)

        # 将总时长分配给两个滑动阶段
        segment_duration_sec = (duration_ms / 2) / 1000

        # 构建动作链
        actions.pointer_action.move_to_location(start_x, element_center_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.pause(segment_duration_sec)  # 第一段滑动

        actions.pointer_action.move_to_location(mid_x, mid_y_with_offset)  # 移动到弧线中点
        actions.pointer_action.pause(segment_duration_sec)  # 第二段滑动

        actions.pointer_action.move_to_location(end_x, element_center_y)  # 移动到终点
        actions.pointer_action.release()

        # 执行手势
        actions.perform()

        allure.attach(
            f"执行带弧度滑动: 从 ({start_x}, {element_center_y}) -> 中点({mid_x}, {mid_y_with_offset}) -> 到 ({end_x}, {element_center_y})",
            name="弧线滑动日志")

    def pinch_in_element(self, locator, direction="out", percent=0.8, duration_ms=500):
        """
        在指定元素上执行双指缩放操作（捏合或放大）
        :param locator: 元素定位器
        :param direction: 'out'缩小/'in'放大
        :param percent: 移动距离比例(0-1)
        :param duration_ms: 动作持续时间(毫秒)
        """
        try:
            # 1. 等待元素可见并获取位置信息
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))
            element = self.driver.find_element(*locator)
            rect = element.rect
            size = self.driver.get_window_size()
            print(f"屏幕尺寸: {size}")
            print(f"元素位置信息: {rect}")

            # 2. 计算地图区域（假设地图占屏幕高度的40%）
            map_height = size['height'] * 0.4
            center_x = size['width'] / 2
            center_y = map_height / 2  # 地图区域的中心点
            offset_x = (size['width'] * percent / 2)  # 基于屏幕宽度的偏移
            offset_y = (map_height * percent / 2)  # 基于地图高度的偏移

            # 3. 设置不同方向的起止点，偏移通知栏和顶部
            notify_bar_offset = 80  # 假设通知栏高度为80像素，可根据设备调整
            start_y_offset = map_height * 0.2  # 从地图顶部向下偏移20%作为起始点
            if direction == "out":
                # 缩小：从外向内移动
                f1_start = (center_x - offset_x, start_y_offset + notify_bar_offset)
                f2_start = (center_x + offset_x, map_height - start_y_offset + notify_bar_offset)
                f1_end = f2_end = (center_x, center_y + notify_bar_offset)
            elif direction == "in":
                # 放大：从内向外移动
                f1_start = f2_start = (center_x, center_y + notify_bar_offset)
                f1_end = (center_x - offset_x, start_y_offset + notify_bar_offset)
                f2_end = (center_x + offset_x, map_height - start_y_offset + notify_bar_offset)
            else:
                raise ValueError("direction参数必须是'in'或'out'")

            # 4. 验证坐标是否在地图区域范围内
            if (f1_start[0] < 0 or f1_start[1] < notify_bar_offset or f2_start[0] < 0 or f2_start[
                1] < notify_bar_offset or
                    f1_end[0] < 0 or f1_end[1] < notify_bar_offset or f2_end[0] < 0 or f2_end[1] < notify_bar_offset or
                    f1_start[0] > size['width'] or f1_start[1] > map_height + notify_bar_offset or
                    f2_start[0] > size['width'] or f2_start[1] > map_height + notify_bar_offset or
                    f1_end[0] > size['width'] or f1_end[1] > map_height + notify_bar_offset or
                    f2_end[0] > size['width'] or f2_end[1] > map_height + notify_bar_offset):
                raise ValueError("坐标超出地图区域范围，请调整percent参数")

            print(f"手指1路径: {f1_start} -> {f1_end}")
            print(f"手指2路径: {f2_start} -> {f2_end}")

            # 5. 创建动作序列，添加曲线路径
            actions = ActionBuilder(self.driver)

            # 第一根手指（添加中间控制点模拟曲线）
            finger1 = actions.add_pointer_input(POINTER_TOUCH, "finger1")
            finger1.create_pointer_move(duration=0, x=int(f1_start[0]), y=int(f1_start[1]))
            finger1.create_pointer_down(button=0)
            # 中间点略微偏移，形成弧形
            mid_x1 = int((f1_start[0] + f1_end[0]) / 2 + (f1_end[1] - f1_start[1]) * 0.2)  # 横向偏移
            mid_y1 = int((f1_start[1] + f1_end[1]) / 2 - (f1_end[0] - f1_start[0]) * 0.2)  # 纵向偏移
            finger1.create_pointer_move(duration=duration_ms // 2, x=mid_x1, y=mid_y1)
            finger1.create_pointer_move(duration=duration_ms // 2, x=int(f1_end[0]), y=int(f1_end[1]))
            finger1.create_pointer_up(button=0)

            # 第二根手指（添加中间控制点模拟曲线）
            finger2 = actions.add_pointer_input(POINTER_TOUCH, "finger2")
            finger2.create_pointer_move(duration=0, x=int(f2_start[0]), y=int(f2_start[1]))
            finger2.create_pointer_down(button=0)
            # 中间点略微偏移，形成弧形
            mid_x2 = int((f2_start[0] + f2_end[0]) / 2 - (f2_end[1] - f2_start[1]) * 0.2)  # 横向偏移
            mid_y2 = int((f2_start[1] + f2_end[1]) / 2 + (f2_end[0] - f2_start[0]) * 0.2)  # 纵向偏移
            finger2.create_pointer_move(duration=duration_ms // 2, x=mid_x2, y=mid_y2)
            finger2.create_pointer_move(duration=duration_ms // 2, x=int(f2_end[0]), y=int(f2_end[1]))
            finger2.create_pointer_up(button=0)

            # 6. 执行动作
            print("正在执行缩放操作...")
            actions.perform()
            time.sleep(2)  # 等待地图控件响应

            # 7. 可选：尝试JavaScript缩放（如果ActionBuilder失败）
            # try:
            #     self.driver.execute_script("mobile: pinch", {
            #         "element": element.id,
            #         "scale": 0.5 if direction == "out" else 2.0,
            #         "velocity": 1.0
            #     })
            #     print("已尝试通过JavaScript执行缩放")
            # except Exception as js_e:
            #     print(f"JavaScript缩放失败: {str(js_e)}")

        except Exception as e:
            print(f"执行缩放操作时出错: {str(e)}")
            raise

        allure.step("点击系统返回键")

    def press_back_key(self):
        """
        调用系统返回键（Back）
        Android 使用 driver.back() 即可
        """
        self.driver.back()
