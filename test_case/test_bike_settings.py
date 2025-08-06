import allure
import pytest
from utils.load_yaml import load_yaml
from page.bike_settings_page import BikeSettingsPage
from page.home_page import HomePage

@allure.epic("velotric app应用")
@allure.story("车辆设置模块")
class TestBikeSettings:
    # 读取测试数据
    data = load_yaml('./data/bike_settings.yaml')

    PAGE_OBJECTS = {
        'HomePage': HomePage,
        'BikeSettingsPage': BikeSettingsPage
    }

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("case", data, ids=[f"{case['case_name']}" for case in data])
    def test_bike_settings(self, bike_settings_page_setup, case):
        allure.dynamic.title(case['case_name'])

        # 获取 driver 和 BikeSettingsPage 的实例
        driver, bsp = bike_settings_page_setup

        # 根据 test_type 分发到不同的处理函数
        test_type = case.get('test_type')

        if test_type == 'change_bike_name':
            TestBikeSettings._run_change_bike_name_test(bsp, case)

        # 可以在这里为未来的测试类型（如更改骑行模式）添加 elif 分支
        # elif test_type == 'change_riding_mode':
        #     TestBikeSettings._run_change_riding_mode_test(bsp, case)

        else:
            pytest.fail(f"框架暂不支持此测试类型或未找到对应的处理函数：'{test_type}'")

        # --- 新增：专门处理“更改车辆名称”测试类型的私有方法 ---
    @staticmethod
    def _run_change_bike_name_test(bsp, case_data):
        """
        执行“更改车辆名称”类型的测试逻辑。
        :param bsp: BikeSettingsPage 的页面实例。
        :param case_data: 当前测试用例的数据字典。
        """
        allure.step(f"执行用例: {case_data['case_name']}")

        # 1. 从用例数据中获取必要信息
        action_method_name = case_data['action_method']
        verify_method_name = case_data['verify_method']
        new_bike_name = case_data['expected_result']  # 期望结果就是我们要输入的新名字

        # 2. 从页面对象中动态获取并执行“操作”方法
        action_method = getattr(bsp, action_method_name)
        action_method(new_bike_name)  # 传入新名字作为参数

        # 3. 从页面对象中动态获取并执行“验证”方法，得到实际结果
        verify_method = getattr(bsp, verify_method_name)
        actual_result = verify_method()

        # 4. 在测试脚本中进行断言
        allure.attach(f"断言：期望结果='{new_bike_name}', 实际结果='{actual_result}'", name="结果断言")
        assert actual_result == new_bike_name, \
            f"车辆名称更改失败！期望为 '{new_bike_name}'，实际为 '{actual_result}'"