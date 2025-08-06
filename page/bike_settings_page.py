import time
import allure
from base.keywords import Keywords
from locator.bike_settings_locator import *


# 车辆设置页
class BikeSettingsPage(Keywords):

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
        allure.attach(f"获取到的当前车辆名称是: '{name}'", name="状态获取")
        return name

    @allure.step("切换到 Eco 模式")
    def click_eco_mode(self):
        allure.attach("步骤 1: 点击 Eco 模式按钮", name="操作日志")
        self.click_element(eco_mode_btn)
        allure.attach("步骤 2: 在NOTICE弹窗中点击 Confirm", name="操作日志")
        self.click_element(mode_confirm_btn)  # 新增点击确认操作
        time.sleep(1)  # 等待UI响应

    @allure.step("切换到 Trail 模式")
    def click_trail_mode(self):
        allure.attach("步骤 1: 点击 Trail 模式按钮", name="操作日志")
        self.click_element(trail_mode_btn)
        allure.attach("步骤 2: 在NOTICE弹窗中点击 Confirm", name="操作日志")
        self.click_element(mode_confirm_btn)  # 新增点击确认操作
        time.sleep(1)

    @allure.step("切换到 Boost 模式")
    def click_boost_mode(self):
        allure.attach("步骤 1: 点击 Boost 模式按钮", name="操作日志")
        self.click_element(boost_mode_btn)
        allure.attach("步骤 2: 在NOTICE弹窗中点击 Confirm", name="操作日志")
        self.click_element(mode_confirm_btn)  # 新增点击确认操作
        time.sleep(1)

    def _get_mode_name_from_element(self, locator):
        """
        一个私有的辅助方法，用于从指定的元素中获取 content-desc 并截取出模式名称。
        """
        try:
            full_text = self.get_element_attribute(locator, 'content-desc')
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