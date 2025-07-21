import allure
from base.keywords import Keywords
from locator.data_sync_locator import *
from locator.help_locator import *
from locator.info_locator import *


# 帮助页
class HelpPage(Keywords):

    @allure.step("点击返回按钮")
    def click_back_btn(self):
        self.click_element(back_btn)

    @allure.step("获取 'Help' 页面的 'HELP' 文案")
    def get_help_text(self):
        return self.get_element_attribute(HELP_TEXT, 'content-desc')
