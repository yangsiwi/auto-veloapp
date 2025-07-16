import time
import allure
from base.keywords import Keywords
from locator.bike_settings_locator import BIKE_SETTINGS_TEXT
from locator.home_locator import *
from locator.info_locator import *


# 车况页【用户首页】
class HomePage(Keywords):
    # 点击首页右上角个人信息按钮
    @allure.step("点击首页右上角个人信息按钮并返回")
    def click_userinfo(self):
        time.sleep(2)
        self.click_element(userinfo_btn)

    @allure.step("点击开始骑行按钮")
    def click_start_riding(self):
        time.sleep(3)
        self.click_element(start_riding_btn)

    @allure.step("点击车辆设置按钮")
    def click_bike_settings(self):
        time.sleep(3)
        self.click_element(bike_settings_btn)

    @allure.step("获取骑行记录页面的 'Settings' 文案")
    def get_settings_text(self):
        settings_ele = self.wait_explicit(SETTINGS_TEXT)
        return settings_ele.get_attribute('content-desc')

    @allure.step("获取车辆设置页面顶部的 'BIKE SETTINGS' 文案")
    def get_bike_settings_content_text(self):
        bike_settings_ele = self.wait_explicit(BIKE_SETTINGS_TEXT)
        return bike_settings_ele.get_attribute('content-desc')
