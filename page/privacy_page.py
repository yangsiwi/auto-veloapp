import allure

from base.keywords import Keywords
from locator.privacy_locator import *


class PrivacyPolicyPage(Keywords):
    @allure.step("点击返回按钮")
    def click_back_btn(self):
        self.click_element(back_btn)

    @allure.step("获取使用条款页面顶部的 'PRIVACY POLICY' 文案")
    def get_privacy_policy_text(self):
        return self.get_element_attribute(PRIVACY_POLICY_TEXT, 'content-desc')
