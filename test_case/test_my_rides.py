import time

import allure
import pytest

from locator.my_rides_locator import *
from page.my_rides_page import MyRidesPage
from utils.load_yaml import load_yaml

class TestMyRides:
    data = load_yaml('./data/my_rides.yaml')

    LOCATORS = {
        'day_tab_btn': day_tab_btn,
        'week_tab_btn': week_tab_btn,
        'month_tab_btn': month_tab_btn,
        'year_tab_btn': year_tab_btn
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
            # 【修正】调用类内部的私有方法
            self._run_scroll_to_bottom(mrp, case)
        elif test_type == 'scroll_top':
            self._run_scroll_to_top(mrp, case)
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

    # 【修正】将滚动测试流程也封装成一个类方法
    def _run_scroll_to_bottom(self, mrp: MyRidesPage, case: dict):
        """处理滚动到页面底部的测试流程"""
        with allure.step("滚动页面到底部"):
            # 直接调用 MyRidesPage 上的滚动方法
            mrp.scroll_to_bottom()
        time.sleep(2)
        # 【优化建议】滚动后最好有一个断言，来验证滚动是否真的发生了
        # 例如，我们可以断言页面底部的某个元素现在可见了
        # with allure.step("断言页面底部元素已可见"):
        #     # 假设有一个 bottom_element_locator
        #     assert mrp.wait_for_element_to_be_visible(bottom_element_locator, timeout=3), \
        #         "滚动到底部后，预期的底部元素未出现"

        # 为了简单起见，我们先只执行滚动操作
        pass

    def _run_scroll_to_top(self, mrp: MyRidesPage, case: dict):
        """处理滚动到页面顶部的测试流程"""
        with allure.step("滚动页面到顶部"):
            # 直接调用 MyRidesPage 上的滚动方法
            mrp.scroll_to_top()

        time.sleep(2)