import allure
import pytest

from page.privacy_page import PrivacyPolicyPage
from utils.load_yaml import load_yaml


@allure.epic("velotric app应用")
@allure.story("隐私政策页面")
class TestPrivacy:
    data = load_yaml('./data/privacy.yaml')

    @pytest.mark.run(order=12)
    @pytest.mark.parametrize("case", data, ids=[f"{case['case_name']}" for case in data])
    def test_terms(self, about_page_setup, case):
        allure.dynamic.title(case['case_name'])

        # 从 fixture 获取已经准备好的 driver 和 InfoPage 实例
        driver, ap = about_page_setup

        test_type = case.get('test_type')
        need_enter = case.get('need_enter_page', True)  # 默认需要进入页面

        if need_enter:
            # 进入到隐私政策页面
            ap.click_privacy_policy()

        # 实例化 Privacy Policy 页面实例
        ppp = PrivacyPolicyPage(driver)

        # --- 核心调度逻辑 ---
        if test_type == 'scroll_bottom':
            TestPrivacy._run_scroll_to_bottom(ppp)
        elif test_type == 'scroll_top':
            TestPrivacy._run_scroll_to_top(ppp)
        else:
            pytest.fail(f"不支持的测试类型：{test_type}")

    @classmethod
    def _run_scroll_to_bottom(cls, ppp):
        ppp.scroll_to_bottom()

    @classmethod
    def _run_scroll_to_top(cls, ppp):
        ppp.scroll_to_top()

        # 退出到 about 页面
        ppp.click_back_btn()
