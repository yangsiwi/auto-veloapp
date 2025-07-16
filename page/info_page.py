import time

from base.keywords import Keywords
from locator.info_locator import back_btn


# 个人信息页
class InfoPage(Keywords):

    def click_back_btn(self):
        time.sleep(1)
        self.click_element(back_btn)
