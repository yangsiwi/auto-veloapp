import allure
from base.keywords import Keywords
from locator.about_velotric_locator import *
from locator.info_locator import *


# 个人信息页
class InfoPage(Keywords):

    @allure.step("点击返回按钮")
    def click_back_btn(self):
        self.click_element(back_btn)

    @allure.step("点击 'About Velotric' 按钮")
    def click_about_velotric(self):
        self.click_element(about_velotric_btn)

    @allure.step("获取 'ABOUT VELOTRIC' 页面的 'ABOUT VELOTRIC' 文案")
    def get_about_velotric_text(self):
        return self.get_element_attribute(ABOUT_VELOTRIC_TEXT, 'content-desc')