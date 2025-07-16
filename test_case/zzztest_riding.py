import time

import allure

from page.HomePage import HomePage
from page.riding_page import RidingPage


@allure.epic("velotric app应用")
@allure.story("开始骑行模块")
class TestRiding:

    def test_riding(self, login):
        time.sleep(5)
        home_page = HomePage(login)
        riding_page = RidingPage(login)
        time.sleep(3)
        home_page.click_start_riding()
        time.sleep(3)
        riding_page.click_resume_btn()


