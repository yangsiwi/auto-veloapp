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
