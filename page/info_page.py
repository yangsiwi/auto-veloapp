import allure
from base.keywords import Keywords
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