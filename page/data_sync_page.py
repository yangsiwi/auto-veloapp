import allure
from base.keywords import Keywords
from locator.data_sync_locator import *
from locator.info_locator import *


# 数据同步页
class DataSyncPage(Keywords):

    @allure.step("点击返回按钮")
    def click_back_btn(self):
        self.click_element(back_btn)

    @allure.step("获取 'DATA SYNCHRONIZATION' 页面的 'DATA SYNCHRONIZATION' 文案")
    def get_data_synchronization_text(self):
        return self.get_element_attribute(DATA_SYNCHRONIZATION_TEXT, 'content-desc')

    @allure.step("点击 'Health Connect' 按钮'")
    def click_health_connect(self):
        self.click_element(health_connect_btn)
