import allure

from base.keywords import Keywords
from locator.health_conn_locator import *


# 安卓 Health Connect 页面
class HealthConnPage(Keywords):

    @allure.step("点击返回按钮")
    def click_back_btn(self):
        self.click_element(back_btn)

    @allure.step("获取 'SYNCHRONIZE WITH ANDROID' 页面的 'SYNCHRONIZE WITH ANDROID' 文案")
    def get_sync_with_android_text(self):
        return self.get_element_attribute(SYNC_WITH_ANDROID_TEXT, 'content-desc')

    @allure.step("点击 'Connect' 按钮'")
    def click_connect_btn(self):
        self.click_element(connect_btn)

    @allure.step("点击 '全部允许' 按钮")
    def click_allow_all_btn(self):
        self.click_element(allow_all_btn)

    @allure.step("点击底部 '允许' 按钮")
    def click_allow_btn(self):
        self.click_element(allow_btn)

    @allure.step("获取 Health Connect 右侧文字")
    def get_health_connect_text(self):
        health_conn_text = self.get_element_attribute(health_connect, 'content-desc')
        connect_status_text = health_conn_text.split('\n')[1]
        return connect_status_text

    @allure.step("点击 '自动同步' 按钮")
    def click_auto_sync_btn(self):
        self.click_element(auto_sync_btn)

    @allure.step("获取 '自动同步' 按钮状态")
    def get_auto_sync_status(self):
        return self.get_element_attribute(auto_sync_btn, 'checked')
