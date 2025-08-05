import time
import allure
import pytest
from page.data_sync_page import DataSyncPage
from page.health_conn_page import HealthConnPage
from utils.load_yaml import load_yaml


@allure.epic("velotric app应用")
@allure.story("数据同步模块")
class TestHealthConn:
    data = load_yaml('./data/health_conn.yaml')

    @pytest.mark.run(order=10)
    @pytest.mark.parametrize("case", data, ids=[f"{case['case_name']}" for case in data])
    def test_health_conn(self, info_page_setup, case):
        allure.dynamic.title(case['case_name'])

        # 从 fixture 获取已经准备好的 driver 和 InfoPage 实例
        driver, ip = info_page_setup
        dsp = DataSyncPage(driver)
        hcp = HealthConnPage(driver)
        # 进入到数据同步页面
        ip.click_data_synchronization()

        # 进入到 SYNCHRONIZE WITH ANDROID 页面
        dsp.click_health_connect()

        # 实例化 DataSyncPage 实例
        dsp = DataSyncPage(driver)

        test_type = case.get('test_type')

        if test_type == 'connect':
            TestHealthConn.__run_click_connect(hcp, case)
        else:
            pytest.fail(f"不支持的测试类型：{test_type}")

        # 断言之后，返回到 InfoPage 页面
        hcp.click_back_btn()
        dsp.click_back_btn()

    @classmethod
    def __run_click_connect(cls, hcp, case):
        """
        处理点击 Connect 按钮
        """
        with allure.step(f"执行点击 Connect 按钮"):
            hcp.click_connect_btn()

        with allure.step(f"执行点击 '全部允许' 按钮"):
            hcp.click_allow_all_btn()

        with allure.step(f"执行点击底部 '允许' 按钮"):
            hcp.click_allow_btn()

        # 暂时不考虑该地方的断言，比较麻烦
        # time.sleep(1)
        with allure.step(f"断言 Health Connect 状态为 Connected"):
            status_text = hcp.get_health_connect_text()
            assert status_text == case['expected_result'], f"期望值: {case['expected_result']}, 实际值: {status_text}"

        with allure.step(f"断言 Auto Synchronize 按钮状态为True"):
            auto_btn_status = hcp.get_auto_sync_status()
            assert auto_btn_status == case[
                'expected_auto_btn_status'], f"期望值: {case['expected_auto_btn_status']} 实际值: {auto_btn_status}"
