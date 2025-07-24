import time
import allure
import pytest
from locator.my_rides_locator import *
from page.my_rides_page import MyRidesPage
from page.ride_detail_page import RideDetailPage
from page.ride_share_page import RideSharePage
from utils.load_yaml import load_yaml
from utils.navigation_helper import run_navigation_test


@allure.epic("velotric app应用")
@allure.feature("分享骑行记录页面")
class TestShare:
    data = load_yaml('./data/ride_share.yaml')

    # LOCATORS = {
    #     'day_tab_btn': day_tab_btn,
    #     'week_tab_btn': week_tab_btn,
    #     'month_tab_btn': month_tab_btn,
    #     'year_tab_btn': year_tab_btn
    # }

    # PAGE_OBJECTS = {
    #     'RideSharePage': RideSharePage
    # }

    @pytest.mark.run(order=6)
    @pytest.mark.parametrize("case", data, ids=[f"{case['case_name']}" for case in data])
    def test_ride_detail(self, ride_share_page_setup, case):
        allure.dynamic.title(case['case_name'])

        # 从 fixture 获取已经准备好的 driver 和 MyRidesPage 实例
        driver, rsp = ride_share_page_setup

        test_type = case.get('test_type')

        # --- 核心调度逻辑 ---
        if test_type == 'swipe_left':
            TestShare._run_scroll_to_left(rsp)
        else:
            pytest.fail(f"不支持的测试类型：{test_type}")

    # --- 私有的、具体的测试流程函数 ---

    @classmethod
    def _run_scroll_to_left(cls, rsp):
        rsp.swipe_card_left()
