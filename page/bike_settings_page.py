import time
import allure
from base.keywords import Keywords
from locator.bike_settings_locator import back_btn
from locator.home_locator import *
from locator.login_locator import *


class BikeSettingsPage(Keywords):

    def click_back_btn(self):
        time.sleep(1)
        self.click_element(back_btn)
