import allure
import pytest
from data.load_excel import pandas_read_excel_dict
from data.load_yaml import load_yaml
from page.LoginPage import LoginPage


@allure.epic("velotric app应用")
@allure.story("登录模块")
class TestCase:
    # 我们的数据在excel中  [{}]的所有excel数据
    # data = pandas_read_excel_dict("./data/velotric.xlsx", 'Sheet1')
    data = load_yaml('./data/login.yaml')
    print("所有的测试数据", data)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("case_data", data)
    def test_login(self, login_driver, case_data):
        # 动态的标题
        allure.dynamic.title(f"{case_data['case_id']}")
        # 实例化登录页 传个设备信息 conftest里面传
        l = LoginPage(login_driver)

        # 获取参数（兼容 Excel 和 YAML 两种数据源）
        all_params = case_data['all_params']

        # 如果是字符串（来自 Excel），用 eval 解析
        if isinstance(all_params, str):
            params = eval(all_params)
        # 如果是字典（来自 YAML），直接使用
        elif isinstance(all_params, dict):
            params = all_params
        else:
            raise ValueError(f"Unsupported data type for all_params: {type(all_params)}")

        # 调用登录方法
        l.login(params['username'], params['password'])

        # 根据用例ID判断是登录成功还是失败场景，并进行断言
        if case_data["case_id"] == 'login003':
            # 登录成功场景验证
            actual_msg = l.success_msg()
            assert actual_msg == case_data["expected_result"], \
                f"期望值: {case_data['expected_result']}, 实际值: {actual_msg}"
        else:
            # 登录失败场景验证
            actual_msg = l.failed_msg()
            assert actual_msg == case_data["expected_result"], \
                f"期望值: {case_data['expected_result']}, 实际值: {actual_msg}"
        # 断言结果输出到报告
        allure.attach(f"预期结果：{case_data['expected_result']}，实际结果：{actual_msg}", name="断言详情")
