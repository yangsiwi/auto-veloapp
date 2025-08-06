import allure
from base.keywords import Keywords
from locator.bike_settings_locator import *
from locator.info_locator import *


# 个人信息页
class InfoPage(Keywords):

    @allure.step("点击返回按钮")
    def click_back_btn(self):
        self.click_element(back_btn)

    @allure.step("点击 'My Rides' 卡片")
    def click_my_rides(self):
        self.click_element(my_rides_card)

    @allure.step("点击 'Account' 按钮")
    def click_account(self):
        self.click_element(account_btn)

    @allure.step("点击 'About Velotric' 按钮")
    def click_about_velotric(self):
        self.click_element(about_velotric_btn)

    @allure.step("点击 'Data Synchronization' 按钮")
    def click_data_synchronization(self):
        self.click_element(data_synchronization_btn)

    @allure.step("点击 'Help' 按钮")
    def click_help(self):
        self.click_element(help_btn)

    @allure.step("点击 'Unit' 按钮")
    def click_unit(self):
        self.click_element(unit_btn)

    @allure.step("在底部弹窗中点击 'Kilometers (km)'")
    def select_kilometers_in_dialog(self):
        self.click_element(kilometers_btn)

    @allure.step("在底部弹窗中点击 'Miles (mi)'")
    def select_miles_in_dialog(self):
        self.click_element(miles_btn)

    @allure.step("获取当前设置的单位文本")
    def get_current_unit_text(self):
        """
        获取"Unit"行的完整content-desc，并从中提取出单位部分。
        """
        # 获取完整的 content-desc, 例如 "Unit\nmiles"
        full_text = self.get_element_attribute(unit_btn, 'content-desc')

        if full_text and '\n' in full_text:
            # 按换行符分割字符串，得到一个列表 ['Unit', 'miles']
            parts = full_text.split('\n')
            # 返回第二个元素，并去除可能的前后空格
            return parts[1].strip()

        # 如果格式不符，返回空字符串或抛出异常
        return ""

    @allure.step("点击 App Version 按钮")
    def click_app_version(self):
        self.click_element(app_version_btn)

    @allure.step("获取个人信息页的 'Settings' 文案")
    def get_settings_text(self):
        return self.get_element_attribute(SETTINGS_TEXT, 'content-desc')
