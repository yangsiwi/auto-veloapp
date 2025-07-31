import allure

from base.keywords import Keywords
# from locator.ride_detail_locator import *
from locator.share_locator import *
from locator.share_locator import *


class RideSharePage(Keywords):

    @allure.step("点击返回按钮")
    def click_back_btn(self):
        self.click_element(back_btn)

    @allure.step("获取顶部 'SHARE MY RIDE' 的文案")
    def get_share_my_ride_text(self):
        return self.get_element_attribute(SHARE_MY_RIDE_TEXT, 'content-desc')

    @allure.step("点击 Share 按钮")
    def click_share_btn(self):
        self.click_element(share_btn)

    @allure.step("获取点击 Share 按钮后系统弹出的'更多'的文案")
    def get_more_text(self):
        return self.get_element_attribute(MORE_TEXT, 'text')

    @allure.step("向左滑动骑行记录卡片")
    def swipe_card_left(self):
        self.swipe_element_horizontally_with_arc(ride_card, direction="left")

    @allure.step("点击 Add image 按钮")
    def click_add_image_btn(self):
        self.click_element(add_image_btn)

    @allure.step("获取点击 Add image 按钮后系统弹窗中的 'Take photo' 按钮的文案")
    def get_take_photo_btn_text(self):
        return self.get_element_attribute(TAKE_PHOTO_TEXT, 'content-desc')

    @allure.step("获取点击 Add image 按钮后系统弹窗中的 'Select from gallery' 按钮的文案")
    def get_select_from_gallery_btn_text(self):
        return self.get_element_attribute(SELECT_FROM_GALLERY_TEXT, 'content-desc')

    @allure.step("点击 Cancel 按钮")
    def click_cancel_btn(self):
        self.click_element(cancel_btn)