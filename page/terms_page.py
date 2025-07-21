import allure

from base.keywords import Keywords
from locator.terms_locator import back_btn, TERMS_OF_USE_TEXT


class TermsOfUsePage(Keywords):

    @allure.step("点击返回按钮")
    def click_back_btn(self):
        self.click_element(back_btn)

    @allure.step("获取使用条款页面顶部的 'TERMS OF USE' 文案")
    def get_terms_of_use_text(self):
        return self.get_element_attribute(TERMS_OF_USE_TEXT, 'content-desc')
