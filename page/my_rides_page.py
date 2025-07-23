import allure
from base.keywords import Keywords
from locator.info_locator import *
from locator.my_rides_locator import *


# 我的骑行页
class MyRidesPage(Keywords):

    @allure.step("点击返回按钮")
    def click_back_btn(self):
        self.click_element(back_btn)

    @allure.step("获取 'My Rides' 页面的 'My Rides' 文案")
    def get_my_rides_text(self):
        return self.get_element_attribute(MY_RIDES_TEXT, 'content-desc')

    @allure.step("点击 day 按钮")
    def click_day_tab(self):
        self.click_element(day_tab_btn)

    @allure.step("点击 Week 按钮")
    def click_week_tab(self):
        self.click_element(week_tab_btn)

    @allure.step("点击 Month 按钮")
    def click_month_tab(self):
        self.click_element(month_tab_btn)

    @allure.step("点击 Year 按钮")
    def click_year_tab(self):
        self.click_element(year_tab_btn)

    @allure.step("获取日期按钮的文案")
    def get_date_tab_text(self, date_tab_btn):
        return self.get_element_attribute(date_tab_btn, 'content-desc')

    @allure.step("滑动到页面底部")
    def scroll_to_bottom(self):
        super().scroll_to_bottom()

    @allure.step("滑动到页面底部")
    def scroll_to_top(self):
        super().scroll_to_top()