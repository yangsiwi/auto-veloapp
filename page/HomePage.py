import time
import allure
from base.keywords import Keywords
from locator.home_locator import *
from locator.info_locator import *
from locator.login_locator import *


class HomePage(Keywords):

    # 点击首页右上角个人信息按钮
    @allure.step("点击首页右上角个人信息按钮")
    def click_personal_information_btn(self):
        time.sleep(5)

        self.click_element(personal_information_btn)

    @allure.step("获取文本")
    def click_success_msg(self):
        settings_ele = self.wait_explicit(settings_text)
        return settings_ele.get_attribute('content-desc')
