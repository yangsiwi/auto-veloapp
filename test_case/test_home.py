import time

import allure
import pytest
from data.load_excel import pandas_read_excel_dict
from data.load_yaml import load_yaml
from page.HomePage import HomePage
from page.LoginPage import LoginPage


@allure.epic("velotric app应用")
@allure.story("首页模块")
class TestHome:
    data = load_yaml('./data/home.yaml')

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("case_data", data, ids=[f"{case['case_id']}-{case['case_name']}" for case in data])
    def test_go_into_personal_info_page(self, login_driver, case_data):
        # 动态的标题
        allure.dynamic.title(f"{case_data['case_id']} - {case_data['case_name']}")

        # 强制等待 3 秒
        time.sleep(3)

        # 实例化 HomePage 对象
        hp = HomePage(login_driver)

        # 点击个人信息按钮
        hp.click_personal_information_btn()

        # 强制等待
        time.sleep(3)

        # 断言【判断进入到个人信息页面中是否有 "Settings" 文字】
        actual_msg = hp.click_success_msg()
        assert actual_msg == case_data[
            "expected_result"], f"期望值: {case_data['expected_result']}, 实际值: {actual_msg}"
