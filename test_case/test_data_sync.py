import allure
import pytest
from page.data_sync_page import DataSyncPage
from page.health_conn_page import HealthConnPage
from utils.load_yaml import load_yaml
from utils.navigation_helper import run_navigation_test


@allure.epic("velotric app应用")
@allure.story("数据同步模块")
class TestDataSync:
    data = load_yaml('./data/data_sync.yaml')

    PAGE_OBJECTS = {
        'DataSyncPage': DataSyncPage,
        'HealthConnPage': HealthConnPage
    }

    @pytest.mark.run(order=9)
    @pytest.mark.parametrize("case", data, ids=[f"{case['case_name']}" for case in data])
    def test_data_sync(self, info_page_setup, case):
        allure.dynamic.title(case['case_name'])

        # 从 fixture 获取已经准备好的 driver 和 InfoPage 实例
        driver, ip = info_page_setup

        # 进入到数据同步页面
        ip.click_data_synchronization()

        # 实例化 DataSyncPage 实例
        dsp = DataSyncPage(driver)

        test_type = case.get('test_type')

        if test_type == 'navigation':
            run_navigation_test(
                driver=driver,
                start_page_object=dsp,
                case_data=case,
                page_object_map=self.PAGE_OBJECTS
            )
        else:
            pytest.fail(f"不支持的测试类型：{test_type}")

        # 断言之后，返回到 InfoPage 页面
        dsp.click_back_btn()
