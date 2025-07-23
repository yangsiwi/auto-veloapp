import time

import allure
import pytest

from locator.my_rides_locator import *
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

        driver, mrp = my_rides_page_setup

        time.sleep(1)
        # 点击 Week 按钮
        ele = self.LOCATORS[case['click_tab_btn']]
        mrp.click_element(ele)
        # 断言获取的文本
        date_tab_text = mrp.get_date_tab_text(ele)
        assert date_tab_text == case['expected_result'], '断言失败'

        time.sleep(1)
