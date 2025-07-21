import allure
import pytest

from page.about_page import AboutPage
from page.info_page import InfoPage
from page.privacy_page import PrivacyPolicyPage
from page.terms_page import TermsOfUsePage
from utils.load_yaml import load_yaml
from utils.navigation_helper import run_navigation_test


@allure.epic("velotric app应用")
@allure.story("关于模块")
class TestAbout:
    data = load_yaml('./data/about.yaml')

    PAGE_OBJECTS = {
        'InfoPage': InfoPage,
        'AboutPage': AboutPage,
        'TermsOfUsePage': TermsOfUsePage,
        'PrivacyPolicyPage': PrivacyPolicyPage
    }

    @pytest.mark.run(order=5)
    @pytest.mark.parametrize("case", data, ids=[f"{case['case_name']}" for case in data])
    def test_info_page_interactions(self, about_page_setup, case):
        """
        通用测试引擎：根据 test_type 分发到不同的测试流程
        """
        allure.dynamic.title(case['case_name'])

        # 从 fixture 获取 driver 和 InfoPage 实例
        driver, ap = about_page_setup

        test_type = case.get('test_type', 'navigation')  # 默认为 navigation

        if test_type == 'navigation':
            run_navigation_test(
                driver=driver,
                start_page_object=ap,
                case_data=case,
                page_object_map=self.PAGE_OBJECTS
            )
        else:
            pytest.fail(f"不支持的测试类型：{test_type}")


