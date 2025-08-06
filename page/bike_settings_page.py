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
