import allure
from base.keywords import Keywords
from locator.about_velotric_locator import *
from locator.info_locator import *


# 关于 Velotric 页
class AboutPage(Keywords):

    @allure.step("点击返回按钮")
    def click_back_btn(self):
        self.click_element(back_btn)

    @allure.step("获取 'ABOUT VELOTRIC' 页面的 'ABOUT VELOTRIC' 文案")
    def get_about_velotric_text(self):
        return self.get_element_attribute(ABOUT_VELOTRIC_TEXT, 'content-desc')

    @allure.step("点击 'Terms of Use' 按钮'")
    def click_terms_of_use(self):
        self.click_element(terms_of_use)

    @allure.step("点击 'Privacy Policy' 按钮")
    def click_privacy_policy(self):
        self.click_element(privacy_policy)
