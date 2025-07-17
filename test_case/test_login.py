import allure
import pytest
from utils.load_yaml import load_yaml
from page.login_page import LoginPage
from locator.login_locator import *


@allure.epic("velotric app应用")
@allure.feature("登录模块")
class TestLogin:
    # 读取测试数据
    test_data = load_yaml('./data/login.yaml')

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("case", test_data, ids=[f"{case['case_name']}" for case in test_data])
    def test_login(self, login_test_driver, case):

        # 动态的标题
        allure.dynamic.title(f"{case['case_name']}")

        # 实例化登录页
        lp = LoginPage(login_test_driver)

        # 获取参数（兼容 Excel 和 YAML 两种数据源）
        all_params = case['all_params']

        # 如果是字符串（来自 Excel），用 eval 解析
        if isinstance(all_params, str):
            params = eval(all_params)
        # 如果是字典（来自 YAML），直接使用
        elif isinstance(all_params, dict):
            params = all_params
        else:
            raise ValueError(f"Unsupported data type for all_params: {type(all_params)}")

        # 调用登录方法
        lp.login(params['username'], params['password'])

        # 根据用例ID判断是登录成功还是失败场景，并进行断言
        # --- 成功场景的处理流程 ---
        if case["case_id"] == 'login003':
            # 获取登录成功的提示信息
            actual_msg = lp.get_success_message()
            assert actual_msg == case["expected_result"], \
                f"期望值: {case['expected_result']}, 实际值: {actual_msg}"
        else:
            # --- 失败场景的处理流程 ---
            # 1. 断言错误信息是否正确
            actual_msg = lp.get_failed_message()
            assert actual_msg == case["expected_result"], \
                f"期望值: {case['expected_result']}, 实际值: {actual_msg}"

            # 2. 断言完成后，显式等待 Toast 消失
            with allure.step("等待错误提示Toast消失"):
                # 我们直接在测试用例中调用底层的关键字，因为这个操作和业务流程强相关
                lp.wait_for_element_to_be_invisible(error_msg)

        # 断言结果输出到报告
        allure.attach(f"预期结果：{case['expected_result']}，实际结果：{actual_msg}", name="断言详情")
