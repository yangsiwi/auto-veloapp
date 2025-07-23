import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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
    def wait_for_element_to_be_visible(self, locator):
        """
        等待元素在页面上可见。
        """
        try:
            return WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                ec.visibility_of_element_located(locator)
            )
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), f"等待元素 {locator} 可见超时",
                          allure.attachment_type.PNG)
            raise TimeoutException(f"等待元素 {locator} 可见超时")

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

    @allure.step("滚动到页面底部 (向上滑动)")
    def scroll_to_bottom(self, duration_ms=600):
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

    @allure.step("滚动到页面顶部 (向下滑动)")
    def scroll_to_top(self, duration_ms=600):
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
