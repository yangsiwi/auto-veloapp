import allure
from base.keywords import Keywords
from locator.info_locator import back_btn


# 个人信息页
class InfoPage(Keywords):

    @allure.step("点击返回按钮")
    def click_back_btn(self):
        self.click_element(back_btn)
