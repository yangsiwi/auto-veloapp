import time
import allure
import pytest
from utils.load_yaml import load_yaml


@allure.epic("velotric app应用")
@allure.feature("分享骑行记录页面")
class TestShare:
    data = load_yaml('./data/ride_share.yaml')

    @pytest.mark.run(order=6)
    @pytest.mark.parametrize("case", data, ids=[f"{case['case_name']}" for case in data])
    def test_ride_detail(self, ride_share_page_setup, case):
        allure.dynamic.title(case['case_name'])

        # 从 fixture 获取已经准备好的 driver 和 MyRidesPage 实例
        driver, rsp = ride_share_page_setup

        test_type = case.get('test_type')

        # --- 核心调度逻辑 ---
        if test_type == 'swipe_left':
            TestShare._run_scroll_to_left(rsp)
        elif test_type == 'click_share_btn':
            TestShare._run_click_share_btn(rsp, case)
        elif test_type == 'click_add_image':
            TestShare._run_click_add_image(rsp, case)
        else:
            pytest.fail(f"不支持的测试类型：{test_type}")

    @classmethod
    def _run_scroll_to_left(cls, rsp):
        rsp.swipe_card_left()

    @classmethod
    def _run_click_share_btn(cls, rsp, case):
        """
        处理点击 Share 按钮后出现底部弹窗的测试流程
        """
        with allure.step(f"执行点击Share按钮"):
            rsp.click_share_btn()

        with allure.step(f"断言弹出页面是否有'更多'文案: {case['expected_result']}"):
            # 断言弹出页面是否有'更多'文案
            actual_msg = rsp.get_more_text()
            assert actual_msg == case['expected_result'], "断言失败"
            # 断言后点击一次返回按钮
            rsp.press_back_key()
            # 强制等待 1 秒
            time.sleep(1)

    @classmethod
    def _run_click_add_image(cls, rsp, case):
        """
        处理点击 Add image 按钮后出现底部弹窗的测试流程
        """
        with allure.step(f"执行点击 Add image 按钮"):
            rsp.click_add_image_btn()

        with allure.step(f"断言弹出页面是否有Take photo文案: {case['expected_result']}"):
            # 断言弹出页面是否有 'Take photo' 的文案
            actual_msg = rsp.get_take_photo_btn_text()
            assert actual_msg == case['expected_result'], "断言失败"
            # 断言完后点击 'Cancel' 按钮
            rsp.click_cancel_btn()
