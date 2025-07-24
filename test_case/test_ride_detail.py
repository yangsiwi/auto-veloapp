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
@allure.feature("骑行记录详情")
class TestRideDetail:
    data = load_yaml('./data/ride_detail.yaml')

    # LOCATORS = {
    #     'day_tab_btn': day_tab_btn,
    #     'week_tab_btn': week_tab_btn,
    #     'month_tab_btn': month_tab_btn,
    #     'year_tab_btn': year_tab_btn
    # }

    PAGE_OBJECTS = {
        'RideSharePage': RideSharePage
    }

    @pytest.mark.run(order=6)
    @pytest.mark.parametrize("case", data, ids=[f"{case['case_name']}" for case in data])
    def test_ride_detail(self, ride_detail_page_setup, case):
        allure.dynamic.title(case['case_name'])

        # 从 fixture 获取已经准备好的 driver 和 MyRidesPage 实例
        driver, rdp = ride_detail_page_setup

        test_type = case.get('test_type')

        # --- 核心调度逻辑 ---
        if test_type == 'zoom_out':
            TestRideDetail._run_zoom_out_map(rdp)
        elif test_type == 'zoom_in':
            TestRideDetail._run_zoom_in_map(rdp)
        elif test_type == 'navigation':
            run_navigation_test(
                driver=driver,
                start_page_object=rdp,
                case_data=case,
                page_object_map=self.PAGE_OBJECTS
            )
        else:
            pytest.fail(f"不支持的测试类型：{test_type}")

    # --- 私有的、具体的测试流程函数 ---

    @staticmethod
    def _run_zoom_out_map(rdp: RideDetailPage):
        """

        """
        time.sleep(5)
        with allure.step("缩小地图"):
            for i in range(5):
                rdp.zoom_out_map()

        time.sleep(3)

    @staticmethod
    def _run_zoom_in_map(rdp: RideDetailPage):
        """

        """
        time.sleep(5)
        for i in range(5):
            with allure.step("缩小地图"):
                rdp.zoom_in_map()

        time.sleep(3)
