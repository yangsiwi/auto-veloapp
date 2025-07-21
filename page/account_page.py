import allure
from base.keywords import Keywords
from locator.about_velotric_locator import *
from locator.account_locator import *
from locator.info_locator import *


# 账户页
class AccountPage(Keywords):

    @allure.step("点击返回按钮")
    def click_back_btn(self):
        self.click_element(back_btn)

    @allure.step("获取 'ACCOUNT' 页面的 'ACCOUNT' 文案")
    def get_account_text(self):
        return self.get_element_attribute(ACCOUNT_TEXT, 'content-desc')

    @allure.step("点击 'Change My Password' 按钮'")
    def click_change_my_password(self):
        self.click_element(change_my_password)

    @allure.step("点击 'Change My Email' 按钮")
    def click_change_my_email(self):
        self.click_element(change_my_email)

    @allure.step("点击 'Delete My Account' 按钮")
    def click_delete_my_account(self):
        self.click_element(delete_my_account)
