import allure

from base.keywords import Keywords


class TermsOfUsePage(Keywords):

    @allure.step("点击返回按钮")
    def click_back_btn(self):
        self.click_element(back_btn)

    @allure.step("点击 'My Rides' 卡片")
    def click_my_rides(self):
        self.click_element(my_rides_card)

    @allure.step("点击 'Account' 按钮")
    def click_account(self):
        self.click_element(account_btn)