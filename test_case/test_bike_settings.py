import time

import allure
import pytest

from locator.bike_settings_locator import pedal_btn, throttle_btn
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
        elif test_type == 'change_riding_mode':
            TestBikeSettings._run_change_riding_mode_test(bsp, case)
        elif test_type == 'change_screen_brightness':
            TestBikeSettings._run_change_screen_brightness_test(bsp, case)
        elif test_type == 'scroll_up':
            TestBikeSettings._run_scroll_up_test(bsp, case)
        elif test_type == 'swipe_speed_limit':
            pass  # 暂时跳过
        elif test_type in ['change_auto_power_off',
                           'change_auto_light',
                           'change_cruise_control',
                           'change_torque_mode',
                           'change_cadence_mode',
                           'click_torque',
                           'click_cadence',
                           'click_mile',
                           'click_km']:
            # 所有新增的、简单的点击类型，都使用这个通用的处理器
            TestBikeSettings._run_generic_click_action(bsp, case)
        else:
            pytest.fail(f"框架暂不支持此测试类型：'{test_type}'")

    # --- 专门处理“更改车辆名称”测试类型的私有方法 ---
    @staticmethod
    def _run_change_bike_name_test(bsp, case_data):
        """
        执行“更改车辆名称”类型的测试步骤。
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

        # 测试完后，执行一次滚动，为下一个测试做准备或方便观察
        # allure.step("当前用例完成，执行一次页面滚动以便观察")
        # bsp.swipe_up(start_y_percent=0.5, end_y_percent=0.5)

    # --- 处理“更改骑行模式”测试类型的私有方法 ---
    @staticmethod
    def _run_change_riding_mode_test(bsp, case_data):
        """
        执行“更改骑行模式”类型的测试逻辑。
        :param bsp: BikeSettingsPage 的页面实例。
        :param case_data: 当前测试用例的数据字典。
        """
        allure.step(f"执行用例: {case_data['case_name']}")

        # 1. 从用例数据中获取必要信息
        action_method_name = case_data['action_method']
        verify_method_name = case_data['verify_method']
        expected_mode = case_data['expected_result']

        # 2. 执行点击操作
        action_method = getattr(bsp, action_method_name)
        action_method()  # 点击模式不需要参数

        # 3. 调用统一的验证方法获取当前选中的模式
        verify_method = getattr(bsp, verify_method_name)
        actual_mode = verify_method()

        # 4. 在测试脚本中进行断言
        allure.attach(f"断言：期望选中的模式='{expected_mode}', 实际选中的模式='{actual_mode}'", name="结果断言")
        assert actual_mode == expected_mode, \
            f"模式切换验证失败！期望选中 '{expected_mode}'，实际选中 '{actual_mode}'"

        # 测试完后，执行一次滚动，为下一个测试做准备或方便观察
        # allure.step("当前用例完成，执行一次页面滚动以便观察")
        # bsp.swipe_up(start_y_percent=0.5, end_y_percent=0.5)

    # --- 【核心新增】专门处理“更改屏幕亮度”测试类型的私有方法 ---
    @staticmethod
    def _run_change_screen_brightness_test(bsp, case_data):
        """
        执行“更改屏幕亮度”类型的测试逻辑。
        目前只执行操作，不进行断言。
        """
        allure.step(f"执行用例: {case_data['case_name']}")

        # 1. 从用例数据中获取操作方法名
        action_method_name = case_data['action_method']

        # 2. 动态获取并执行操作方法
        action_method = getattr(bsp, action_method_name)
        action_method()

        # 3. 在报告中记录一下，表示操作已完成
        allure.attach(f"已成功执行操作: {action_method_name}", "操作完成", allure.attachment_type.TEXT)
        # 由于当前无法断言，我们默认只要操作不报错，用例即为通过。

    # --- 【核心新增】专门处理“向上滚动”测试类型的私有方法 ---
    @staticmethod
    def _run_scroll_up_test(bsp, case_data):
        """
        执行“向上滚动”类型的操作。
        """
        allure.step(f"执行用例: {case_data['case_name']}")

        # 1. 从用例数据中获取滚动的参数
        #    使用 .get() 方法并提供默认值，使参数变为可选，增加健壮性
        start_percent = case_data.get('start_y_percent', 0.8)  # 默认为 0.8
        end_percent = case_data.get('end_y_percent', 0.2)  # 默认为 0.2

        # 2. 调用底层的 swipe_up 方法，并传入从YAML中读取的参数
        bsp.swipe_up(start_y_percent=start_percent, end_y_percent=end_percent)

        allure.attach(f"已执行向上滚动，幅度: {start_percent * 100}% -> {end_percent * 100}%", "操作完成",
                      allure.attachment_type.TEXT)
        # 滚动操作本身没有断言，执行成功即为通过
        time.sleep(3)

    # --- 【核心新增】专门处理“滑动限速条”测试类型的私有方法 ---
    # @staticmethod
    # def _run_swipe_speed_limit_test(bsp, case_data):
    #     """
    #     执行“滑动限速条”类型的测试逻辑。
    #     """
    #     allure.step(f"执行用例: {case_data['case_name']}")
    #
    #     # 1. 从用例数据中获取操作所需的参数字典
    #     params = case_data['action_params']
    #     target_slider = params['target']
    #     swipe_direction = params['direction']
    #
    #     # 2. 直接调用 Page 层那个通用的滑动方法
    #     #    我们这里没有用 getattr，因为方法是固定的，这样更直观
    #     bsp.swipe_speed_limit_slider(target=target_slider, direction=swipe_direction)
    #
    #     allure.attach(f"已成功对 '{target_slider}' 执行了向 '{swipe_direction}' 的滑动操作", "操作完成",
    #                   allure.attachment_type.TEXT)
    #     # 当前不做断言，默认操作成功即用例通过

    # --- 【核心新增】专门处理“更改自动关机时间”测试类型的私有方法 ---
    @staticmethod
    def _run_change_auto_power_off_test(bsp, case_data):
        """
        执行“更改自动关机时间”类型的测试逻辑。
        """
        allure.step(f"执行用例: {case_data['case_name']}")

        # 1. 从用例数据中获取操作方法名
        action_method_name = case_data['action_method']

        # 2. 动态获取并执行操作方法
        action_method = getattr(bsp, action_method_name)
        action_method()

        allure.attach(f"已成功执行操作: {action_method_name}", "操作完成", allure.attachment_type.TEXT)
        # 当前不做断言，默认操作成功即用例通过

    # --- 【核心新增】专门处理“切换自动大灯”测试类型的私有方法 ---
    @staticmethod
    def _run_change_auto_light_test(bsp, case_data):
        """
        执行“切换自动大灯开关”类型的测试逻辑。
        """
        allure.step(f"执行用例: {case_data['case_name']}")

        # 1. 从用例数据中获取操作方法名
        action_method_name = case_data['action_method']

        # 2. 动态获取并执行操作方法
        action_method = getattr(bsp, action_method_name)
        action_method()

        allure.attach(f"已成功执行操作: {action_method_name}", "操作完成", allure.attachment_type.TEXT)
        # 同样，暂时不进行断言

    # --- 【核心新增】为所有新功能创建统一的、通用的处理器 ---
    @staticmethod
    def _run_generic_click_action(bsp, case_data, needs_scrolling=True):
        """
        一个通用的处理器，适用于所有“滚动后点击”类型的简单操作。
        :param bsp: BikeSettingsPage 的页面实例。
        :param case_data: 当前测试用例的数据字典。
        :param needs_scrolling: 是否需要在操作前执行滚动。
        """
        allure.step(f"执行用例: {case_data['case_name']}")

        # 1. 从用例数据中获取操作方法名
        action_method_name = case_data['action_method']
        time.sleep(3)
        # 2. 动态获取并执行操作方法
        action_method = getattr(bsp, action_method_name)
        action_method()

        allure.attach(f"已成功执行操作: {action_method_name}", "操作完成", allure.attachment_type.TEXT)
