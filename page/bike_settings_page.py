import time
import allure
from base.keywords import Keywords
from locator.bike_settings_locator import *


# 车辆设置页
class BikeSettingsPage(Keywords):

    @allure.step("点击返回按钮")
    def click_back_btn(self):
        time.sleep(1)
        self.click_element(back_btn)

    @allure.step("获取车辆设置页面顶部的 'BIKE SETTINGS' 文案")
    def get_bike_settings_content_text(self):
        return self.get_element_attribute(BIKE_SETTINGS_TEXT, 'content-desc')

    @allure.step("执行修改车辆名称的操作")
    def change_bike_name(self, new_name):
        """
        封装了更改车辆名称的完整操作流程。
        :param new_name:要设置的新的车辆名称。
        """
        # 1. 点击车辆名称旁边的编辑图标
        allure.attach("步骤 1: 点击编辑图标", name="操作日志")
        self.click_element(edit_bike_name)
        # 虽然车辆名称通常在顶部，但使用滚动查找能让代码更健壮
        # bike_name_element = self.scroll_to_find_element(edit_bike_name)
        # bike_name_element.click()

        # 2. 在弹出的输入框中，先点击'x'清空，然后输入新名字
        allure.attach(f"步骤 2: 输入新名称 '{new_name}'", name="操作日志")
        # 注意：这里的清空和输入封装在 keywords.py 中，非常方便
        self.clear_and_input_text(bike_name_input, new_name)

        # 3. 点击弹窗的确定按钮
        allure.attach("步骤 3: 点击确定按钮", name="操作日志")
        self.click_element(bike_name_confirm_btn)

        # 短暂等待UI刷新
        time.sleep(1)

    @allure.step("获取当前显示的车辆名称")
    def get_bike_name_text(self):
        """
        获取车辆名称显示区域的文本。
        :return: 返回当前显示的车辆名称字符串。
        """
        # 我们从 content-desc 属性中获取名称
        name = self.get_element_attribute(edit_bike_name, 'content-desc')
        # bike_name_element = self.scroll_to_find_element(edit_bike_name)
        # name = bike_name_element.get_attribute('content-desc')
        allure.attach(f"获取到的当前车辆名称是: '{name}'", name="状态获取")
        return name

    @allure.step("切换到 Eco 模式")
    def click_eco_mode(self):
        time.sleep(2)
        allure.attach("步骤 1: 点击 Eco 模式按钮", name="操作日志")
        self.click_element(eco_mode_btn)
        # eco_element = self.scroll_to_find_element(eco_mode_btn)
        # eco_element.click()
        allure.attach("步骤 2: 在NOTICE弹窗中点击 Confirm", name="操作日志")
        self.click_element(mode_confirm_btn)  # 新增点击确认操作
        time.sleep(1)  # 等待UI响应

    @allure.step("切换到 Trail 模式")
    def click_trail_mode(self):
        allure.attach("步骤 1: 点击 Trail 模式按钮", name="操作日志")
        self.click_element(trail_mode_btn)
        # trail_element = self.scroll_to_find_element(trail_mode_btn)
        # trail_element.click()
        allure.attach("步骤 2: 在NOTICE弹窗中点击 Confirm", name="操作日志")
        self.click_element(mode_confirm_btn)  # 新增点击确认操作
        time.sleep(1)

    @allure.step("切换到 Boost 模式")
    def click_boost_mode(self):
        allure.attach("步骤 1: 点击 Boost 模式按钮", name="操作日志")
        self.click_element(boost_mode_btn)
        # boost_element = self.scroll_to_find_element(boost_mode_btn)
        # boost_element.click()
        allure.attach("步骤 2: 在NOTICE弹窗中点击 Confirm", name="操作日志")
        self.click_element(mode_confirm_btn)  # 新增点击确认操作
        time.sleep(1)

    def _get_mode_name_from_element(self, locator):
        """
        用于从指定的元素中获取 content-desc 并截取出模式名称。
        """
        try:
            full_text = self.get_element_attribute(locator, 'content-desc')
            # element = self.scroll_to_find_element(locator)
            # full_text = element.get_attribute('content-desc')
            # 按换行符分割，并取第一部分
            mode_name = full_text.split('\n')[0]
            allure.attach(f"从元素 {locator} 获取到模式名称: '{mode_name}'", name="状态获取")
            return mode_name
        except Exception as e:
            allure.attach(f"从元素 {locator} 获取文本失败, 错误: {e}", name="验证失败")
            return "获取文本失败"

    @allure.step("获取 Eco 模式元素的名称")
    def get_eco_mode_text(self):
        return self._get_mode_name_from_element(eco_mode_btn)

    @allure.step("获取 Trail 模式元素的名称")
    def get_trail_mode_text(self):
        return self._get_mode_name_from_element(trail_mode_btn)

    @allure.step("获取 Boost 模式元素的名称")
    def get_boost_mode_text(self):
        return self._get_mode_name_from_element(boost_mode_btn)

    @allure.step("点击屏幕亮度 '1' 档")
    def click_screen_brightness_1(self):
        # 使用滚动查找来确保按钮可见，然后点击
        self.click_element(screen_brightness_btn_1)
        time.sleep(1)  # 点击后等待一下

    @allure.step("点击屏幕亮度 '2' 档")
    def click_screen_brightness_2(self):
        self.click_element(screen_brightness_btn_2)
        time.sleep(1)

    @allure.step("点击屏幕亮度 '3' 档")
    def click_screen_brightness_3(self):
        self.click_element(screen_brightness_btn_3)
        time.sleep(1)

    @allure.step("点击屏幕亮度 '4' 档")
    def click_screen_brightness_4(self):
        self.click_element(screen_brightness_btn_4)
        time.sleep(1)

    @allure.step("点击屏幕亮度 '5' 档")
    def click_screen_brightness_5(self):
        self.click_element(screen_brightness_btn_5)
        time.sleep(1)

    @allure.step("点击屏幕亮度 'Auto' 档")
    def click_screen_brightness_auto(self):
        self.click_element(screen_brightness_btn_auto)
        # time.sleep(3)
        # self.swipe_up(start_y_percent=0.6, end_y_percent=0.4)
        time.sleep(1)

    # --- 通用的、数据驱动的滑动条操作方法 ---
    # --- 【核心修改】重构滑动条操作方法，改用“分步拖拽”逻辑 ---
    # @allure.step("拖动限速滑块: 目标 '{target}', 方向 '{direction}'")
    # def swipe_speed_limit_slider(self, target: str, direction: str):
    #     """
    #     一个通用的方法，通过“分步拖拽”来操作 Pedal 或 Throttle 的滑块。
    #     """
    #     locator_map = {
    #         "pedal": pedal_btn,
    #         "throttle": throttle_btn
    #     }
    #     target_locator = locator_map.get(target.lower())
    #
    #     if not target_locator:
    #         raise ValueError(f"无效的滑动目标: '{target}'。")
    #
    #     # 调用 keywords 中全新的“分步拖拽”方法
    #     self.drag_element_in_steps(target_locator, direction=direction)
    #
    #     time.sleep(1)  # 操作后等待UI响应

    @allure.step("点击 Auto Power Off 'OFF' 档")
    def click_auto_power_off_off(self):
        # 这个元素通常在页面下方，但我们让测试脚本来处理滚动
        self.click_element(auto_power_off_off_btn)
        time.sleep(1)

    @allure.step("点击 Auto Power Off '5' 分钟档")
    def click_auto_power_off_5(self):
        self.click_element(auto_power_off_5_btn)
        time.sleep(1)

    @allure.step("点击 Auto Power Off '10' 分钟档")
    def click_auto_power_off_10(self):
        self.click_element(auto_power_off_10_btn)
        time.sleep(1)

    @allure.step("点击 Auto Power Off '30' 分钟档")
    def click_auto_power_off_30(self):
        self.click_element(auto_power_off_30_btn)
        time.sleep(1)

    @allure.step("点击 Auto Power Off '60' 分钟档")
    def click_auto_power_off_60(self):
        self.click_element(auto_power_off_60_btn)
        time.sleep(1)

    # --- 【核心新增】切换 Auto Light 开关的操作方法 ---

    @allure.step("点击 Auto Light 开关")
    def click_auto_light(self):
        # 这个元素在页面最底部，我们让测试脚本来处理滚动
        self.click_element(auto_light_btn)
        time.sleep(1)

    # --- 【核心新增】最后批次的所有操作方法 ---

    # Cruise Control
    @allure.step("点击 Cruise Control 开关")
    def click_cruise_control(self):
        self.click_element(cruise_control_btn)
        time.sleep(1)

    # Throttle Limit
    @allure.step("点击 Torque Mode 开关")
    def click_torque_mode(self):
        self.click_element(torque_mode_btn)
        time.sleep(1)

    @allure.step("点击 Cadence Mode 开关")
    def click_cadence_mode(self):
        self.click_element(cadence_mode_btn)
        time.sleep(1)

    # SensorSwap
    @allure.step("点击 SensorSwap 的 Torque 按钮")
    def click_torque_btn(self):
        self.click_element(torque_sensor_swap_btn)
        time.sleep(1)

    @allure.step("点击 SensorSwap 的 Cadence 按钮")
    def click_cadence_btn(self):
        self.click_element(cadence_sensor_swap_btn)
        time.sleep(1)

    # Set Unit
    @allure.step("点击 Set Unit 的 Mile 按钮")
    def click_mile_btn(self):
        self.click_element(mile_unit_btn)
        time.sleep(1)

    @allure.step("点击 Set Unit 的 Km 按钮")
    def click_km_btn(self):
        self.click_element(km_unit_btn)
        time.sleep(1)