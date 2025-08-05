import allure
import pytest
from page.terms_page import TermsOfUsePage
from utils.load_yaml import load_yaml


@allure.epic("velotric app应用")
@allure.story("使用条款页面")
class TestTerms:
    data = load_yaml('./data/terms.yaml')

    @pytest.mark.run(order=11)
    @pytest.mark.parametrize("case", data, ids=[f"{case['case_name']}" for case in data])
    def test_terms(self, about_page_setup, case):
        allure.dynamic.title(case['case_name'])

        # 从 fixture 获取已经准备好的 driver 和 InfoPage 实例
        driver, ap = about_page_setup

        test_type = case.get('test_type')
        need_enter = case.get('need_enter_page', True)  # 默认需要进入页面

        if need_enter:
            # 进入到 Terms of Use 页面
            ap.click_terms_of_use()

        # 实例化 Terms of Use 页面实例
        tp = TermsOfUsePage(driver)

        # --- 核心调度逻辑 ---
        if test_type == 'scroll_bottom':
            TestTerms._run_scroll_to_bottom(tp)
        elif test_type == 'scroll_top':
            TestTerms._run_scroll_to_top(tp)
        else:
            pytest.fail(f"不支持的测试类型：{test_type}")

    @classmethod
    def _run_scroll_to_bottom(cls, tp):
        tp.scroll_to_bottom()

    @classmethod
    def _run_scroll_to_top(cls, tp):
        tp.scroll_to_top()
