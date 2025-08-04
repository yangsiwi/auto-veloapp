import time
import allure
import pytest
from locator.my_rides_locator import *
from page.my_rides_page import MyRidesPage
from page.ride_detail_page import RideDetailPage
from utils.load_yaml import load_yaml
from utils.navigation_helper import run_navigation_test

@allure.epic("velotric app应用")
@allure.story("我的骑行记录模块")
class TestMyRides:
    data = load_yaml('./data/my_rides.yaml')

    LOCATORS = {
        'day_tab_btn': day_tab_btn,
        'week_tab_btn': week_tab_btn,
        'month_tab_btn': month_tab_btn,
        'year_tab_btn': year_tab_btn
    }

    PAGE_OBJECTS = {
        'RideDetailPage': RideDetailPage
    }

    @pytest.mark.run(order=6)
    @pytest.mark.parametrize("case", data, ids=[f"{case['case_name']}" for case in data])
    def test_click_data_tab(self, my_rides_page_setup, case):
        allure.dynamic.title(case['case_name'])

        # 从 fixture 获取已经准备好的 driver 和 MyRidesPage 实例
        driver, mrp = my_rides_page_setup

        test_type = case.get('test_type')

        # --- 核心调度逻辑 ---
        if test_type == 'switch':
            self._run_switch_date(mrp, case)
        elif test_type == 'scroll_bottom':
            TestMyRides._run_scroll_to_bottom(mrp)
        elif test_type == 'swipe_right':
            TestMyRides._run_scroll_to_right(mrp)
        elif test_type == 'swipe_left':
            TestMyRides._run_scroll_to_left(mrp)
        elif test_type == 'navigation':
            run_navigation_test(
                driver=driver,
                start_page_object=mrp,
                case_data=case,
                page_object_map=self.PAGE_OBJECTS
            )
            time.sleep(10)
        else:
            pytest.fail(f"不支持的测试类型：{test_type}")

    # --- 私有的、具体的测试流程函数 ---

    def _run_switch_date(self, mrp: MyRidesPage, case: dict):
        """处理日期标签切换的测试流程"""
        # 点击前可以先加一个等待，让页面更稳定
        time.sleep(1)

        with allure.step(f"点击切换日期: {case['click_tab_btn']}"):
            # 从LOCATORS字典中获取定位器
            locator_to_click = self.LOCATORS[case['click_tab_btn']]
            mrp.click_element(locator_to_click)

        # 点击后也加一个等待，等待UI和数据刷新
        time.sleep(1)

        with allure.step(f"断言切换后的文本为: '{case['expected_result']}'"):
            # 断言时，我们不再需要get_date_tab_text，可以直接验证按钮的属性
            # 但为了保持一致性，使用get_date_tab_text也可以
            actual_text = mrp.get_date_tab_text(locator_to_click)
            assert actual_text == case['expected_result'], \
                f"断言失败, 期望: '{case['expected_result']}', 实际: '{actual_text}'"

        # 【核心】在方法定义前加上 @staticmethod 装饰器

    @staticmethod
    def _run_scroll_to_bottom(mrp: MyRidesPage):
        """
        处理滚动到底部并验证最后一条记录的测试流程。
        这是一个静态方法，它的行为不依赖于TestMyRides的任何实例状态。
        """
        with allure.step("步骤一：执行智能滚动，确保到达列表底部"):
            mrp.scroll_to_list_bottom()
        with allure.step("步骤二：获取并验证最后一条记录"):
            last_ride_text = mrp.get_last_ride_card_text()
            allure.attach(f"成功滚动到底部，获取到最后一条记录: {last_ride_text}", name="验证结果")
            assert last_ride_text is not None and len(last_ride_text) > 0, \
                "已滚动到底部，但未能获取到最后一条记录的文本。"

        time.sleep(3)

    @staticmethod
    def _run_scroll_to_right(mrp: MyRidesPage):
        with allure.step("向右滑动"):
            mrp.swipe_chart_right()
        time.sleep(5)

    @staticmethod
    def _run_scroll_to_left(mrp: MyRidesPage):
        with allure.step("向左滑动"):
            mrp.swipe_chart_left()
        time.sleep(5)