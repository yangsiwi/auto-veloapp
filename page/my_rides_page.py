import allure
import pytest
from selenium.common import TimeoutException

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

    @allure.step("滚动到页面最底部")
    def scroll_to_list_bottom(self):
        """
        调用底层的智能滚动方法，确保滚动到列表的尽头。
        """
        self.scroll_to_very_bottom()

    # 一个专门用于获取最后一条记录的方法
    @allure.step("获取最后一条骑行记录的文本")
    def get_last_ride_card_text(self):
        """
        获取当前可见的最后一条骑行记录的文本。
        【注意】调用此方法前，应确保已滚动到底部。
        """
        # 使用我们之前设计的 LAST_RIDE_CARD_ITEM 定位器
        try:
            last_element = self.wait_for_element_to_be_visible(LAST_RIDE_CARD_ITEM)
            return last_element.get_attribute('content-desc')
        except TimeoutException:
            pytest.fail("在页面上找不到最后一条骑行记录的元素。")

    @allure.step("点击最后一条骑行记录卡片")
    def click_last_ride_card(self):
        self.click_element(LAST_RIDE_CARD_ITEM)

    @allure.step("向左滑动骑行图表")
    def swipe_chart_left(self):
        # 妈的要带弧度的水平滑动，不然图表不会动，太变态了。
        self.swipe_element_horizontally_with_arc(RIDE_CHART, direction="left")

    @allure.step("向右滑动骑行图表")
    def swipe_chart_right(self):
        # 先点击元素
        # self.click_element(RIDE_CHART)
        # 再进行滑动
        # for i in range(3):
        #     self.swipe_element_horizontally(RIDE_CHART, direction="right")
        # 妈的要带弧度的水平滑动，不然图表不会动，太变态了。
        self.swipe_element_horizontally_with_arc(RIDE_CHART, direction="right")