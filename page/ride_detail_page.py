import allure

from base.keywords import Keywords
from locator.ride_detail_locator import *


class RideDetailPage(Keywords):

    @allure.step("点击返回按钮")
    def click_back_btn(self):
        self.click_element(back_btn)

    @allure.step("获取 Share 按钮的文案")
    def get_share_btn_text(self):
        return self.get_element_attribute(share_btn, 'content-desc')

    @allure.step("缩小地图")
    def zoom_out_map(self):
        self.pinch_in_element(map_locator, "out")

    @allure.step("放大地图")
    def zoom_in_map(self):
        self.pinch_in_element(map_locator, "in")

    @allure.step("点击 Share 按钮")
    def click_share_btn(self):
        self.click_element(share_btn)
