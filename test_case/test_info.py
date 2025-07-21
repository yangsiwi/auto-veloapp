import time
import allure
import pytest
from conftest import info_page_setup
from locator.info_locator import *
from page.help_page import HelpPage
from utils.load_yaml import load_yaml
from page.about_page import AboutPage
from page.account_page import AccountPage
from page.my_rides_page import MyRidesPage
from page.data_sync_page import DataSyncPage


@allure.epic("velotric app应用")
@allure.story("个人信息模块")
class TestInfo:
    # 加载所有数据
    all_info_data = load_yaml('./data/info.yaml')

    # 创建一个 Page Object 的映射字典
    # 键是 YAML 中的字符串，值是真正的页面类
    PAGE_OBJECTS = {
        'MyRidesPage': MyRidesPage,
        'AccountPage': AccountPage,
        'AboutPage': AboutPage,
        'DataSyncPage': DataSyncPage,
        'HelpPage': HelpPage
    }

    LOCATORS = {
        'kilometers_btn': kilometers_btn,
        'miles_btn': miles_btn,
        'app_version_toast': app_version_toast,
    }

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("case", all_info_data, ids=[f"{case['case_name']}" for case in all_info_data])
    def test_info_page_interactions(self, info_page_setup, case):
        """
        通用测试引擎：根据 test_type 分发到不同的测试流程
        """
        allure.dynamic.title(case['case_name'])

        # 从 fixture 获取 driver 和 InfoPage 实例
        driver, ip = info_page_setup

        test_type = case.get('test_type', 'navigation')  # 默认为 navigation

        if test_type == 'navigation':
            self._run_navigation_test(driver, ip, case)
        elif test_type == 'bottom_dialog':
            # 将ip对象也传进去
            self._run_bottom_dialog_test(ip, case)
        elif test_type == 'toast_message':
            self._run_toast_test(ip, case)
        else:
            pytest.fail(f"不支持的测试类型：{test_type}")

    # --- 私有测试流程实现 ---
    def _run_navigation_test(self, driver, ip, case):
        """
        处理导航到子页面的测试流程
        """

        # 从 YAML 获取需要实例化的页面类名，并通过字典找到对应的类
        NextPageClass = self.PAGE_OBJECTS[case['page_object_name']]
        # 实例化目标页面对象
        next_page = NextPageClass(driver)

        with allure.step(f"执行点击: {case['click_method']}"):
            # 使用 getattr 动态调用 InfoPage 上面的点击方法
            getattr(ip, case['click_method'])()
            # 上面的写法等同于以下的写法
            # info_page_click_method = getattr(ip, case['click_method'])
            # info_page_click_method()

        with allure.step(f"断言页面标题为: {case['expected_result']}"):
            actual_msg = getattr(next_page, case['verify_method'])()
            assert actual_msg == case['expected_result'], f"期望值: {case['expected_result']}, 实际值: {actual_msg}"

        with allure.step("返回到个人信息页"):
            time.sleep(3)
            next_page.click_back_btn()

    def _run_bottom_dialog_test(self, ip, case): # 参数简化
        """
        处理点击后出现底部弹窗的测试流程
        """
        with allure.step(f"执行点击: {case['click_method']}"):
            getattr(ip, case['click_method'])()

        with allure.step("在弹窗中执行操作"):
            action_locator = self.LOCATORS[case['action_locator_name']]
            ip.click_element(action_locator)

        with allure.step(f"断言主页面状态已更新为: {case['expected_result']}"):
            # 【核心修正】通过 getattr 动态调用 InfoPage 上的验证方法
            verify_method = getattr(ip, case['verify_method'])
            actual_msg = verify_method()
            assert actual_msg == case['expected_result'], "主页面状态断言失败"

    def _run_toast_test(self, ip, case):
        """
        处理点击后出现 Toast 消息的测试流程
        """
        with allure.step(f"执行点击: {case['click_method']}"):
            getattr(ip, case['click_method'])()

        # 从 LOCATORS 字典获取"Toast"的定位器
        toast_locator = self.LOCATORS[case['verify_locator_name']]

        with allure.step(f"断言Toast消息为: '{case['expected_result']}'"):
            # 1. 验证"Toast"出现，并获取其文本进行断言
            actual_msg = ip.get_element_attribute(toast_locator, 'content-desc')
            assert actual_msg == case['expected_result'], "Toast消息文本断言失败"

        with allure.step("等待Toast消息消失"):
            # 2. 等待同一个定位器对应的元素从页面上消失
            assert ip.wait_for_element_to_be_invisible(toast_locator, timeout=5), "Toast消息未按预期消失"

    # 使用合并后的数据进行参数化
    # @pytest.mark.parametrize("case", all_subpage_data, ids=[f"{case['case_name']}" for case in all_subpage_data])
    # def test_subpage_navigation(self, info_page_setup, case):
    #     """
    #     【通用引擎】测试从个人信息页到子页面的导航和返回
    #     """
    #     allure.dynamic.title(case['case_name'])
    #
    #     # 从 fixture 直接解包获取 driver 和已经实例化好的 ip 对象
    #     driver, ip = info_page_setup
    #
    #     # 从 YAML 获取需要实例化的页面类名，并通过字典找到对应的类
    #     NextPageClass = self.PAGE_OBJECTS[case['page_object_name']]
    #     # 实例化目标页面对象
    #     next_page = NextPageClass(driver)
    #
    #     with allure.step(f"{case['case_name']}"):
    #         # 【核心】使用 getattr 动态调用 InfoPage 上面的点击方法
    #         info_page_click_method = getattr(ip, case['click_method'])
    #         info_page_click_method()
    #
    #     with allure.step("断言是否成功进入到子页面"):
    #         # 【核心】使用 getattr 动态调用目标页面上的验证方法
    #         next_page_verify_method = getattr(next_page, case['verify_method'])
    #         actual_msg = next_page_verify_method()
    #         assert actual_msg == case['expected_result'], f"期望值: {case['expected_result']}, 实际值: {actual_msg}"
    #
    #     with allure.step("逐层返回，恢复App到主页状态"):
    #         # 【核心】next_page 是动态的，但是 back_btn 方法是所有子页面共有的
    #         next_page.click_back_btn()

# # 读取测试数据
# test_data = load_yaml('./data/info.yaml')
# my_rides_data = test_data['my_rides_data']
# account_data = test_data['account_data']
# about_velotric_data = test_data['about_velotric_data']
#
# @pytest.mark.run(order=4)
# @pytest.mark.parametrize("case_data", my_rides_data, ids=[f"{case['case_name']}" for case in my_rides_data])
# def test_click_my_rides_card(self, logged_in_driver, case_data):
#     """
#     测试点击 "My Rides" 卡片进入到子页面。
#     """
#
#     # 动态的标题
#     allure.dynamic.title(f"{case_data['case_name']}")
#
#     # 实例化 HomePage、InfoPage、AboutPage 对象
#     hp = HomePage(logged_in_driver)
#     ip = InfoPage(logged_in_driver)
#     mrp = MyRidesPage(logged_in_driver)
#
#     # 在首页点击"个人信息"按钮
#     hp.click_userinfo()
#
#     # 在个人信息页点击 "My Rides" 卡片
#     ip.click_my_rides()
#
#     # 断言是否成功进入 "My Rides" 页
#     # 判断进入到 "My Rides" 页面中是否有 "MY RIDES" 文字】
#     actual_msg = mrp.get_my_rides_text()
#     assert actual_msg == case_data[
#         "expected_result"], f"期望值: {case_data['expected_result']}, 实际值: {actual_msg}"
#
#     mrp.click_back_btn()
#     ip.click_back_btn()
#
# @pytest.mark.run(order=4)
# @pytest.mark.parametrize("case_data", account_data,
#                          ids=[f"{case['case_name']}" for case in account_data])
# def test_click_account(self, logged_in_driver, case_data):
#     """
#     测试点击 "Account" 进入到子页面
#     """
#     # 动态的标题
#     allure.dynamic.title(f"{case_data['case_name']}")
#
#     # 实例化页面对象
#     hp = HomePage(logged_in_driver)
#     ip = InfoPage(logged_in_driver)
#     ap = AccountPage(logged_in_driver)
#
#     # 在首页点击"个人信息"按钮
#     hp.click_userinfo()
#
#     # 在个人信息页面点击 "Account" 按钮
#     ip.click_account()
#
#     # 断言是否成功进入ABOUT VELOTRIC页【判断进入到ABOUT VELOTRIC页面中是否有 "ABOUT VELOTRIC" 文字】
#     actual_msg = ap.get_account_text()
#     assert actual_msg == case_data[
#         "expected_result"], f"期望值: {case_data['expected_result']}, 实际值: {actual_msg}"
#
#     # 断言完成后，在个人信息页面点击返回按钮回到主页
#     ap.click_back_btn()
#     ip.click_back_btn()
#
# @pytest.mark.run(order=5)
# @pytest.mark.parametrize("case_data", about_velotric_data,
#                          ids=[f"{case['case_name']}" for case in about_velotric_data])
# def test_click_about_velotric(self, logged_in_driver, case_data):
#     """
#     测试点击 "about velotric" 能进入到子页面。
#     """
#
#     # 动态的标题
#     allure.dynamic.title(f"{case_data['case_name']}")
#
#     # 实例化页面对象
#     hp = HomePage(logged_in_driver)
#     ip = InfoPage(logged_in_driver)
#     ap = AboutPage(logged_in_driver)
#
#     # 在首页点击"个人信息"按钮
#     hp.click_userinfo()
#
#     ip.click_about_velotric()  # 在个人信息页点击 "About Velotric" 按钮
#     # 断言是否成功进入ABOUT VELOTRIC页【判断进入到ABOUT VELOTRIC页面中是否有 "ABOUT VELOTRIC" 文字】
#     actual_msg = ap.get_about_velotric_text()
#     assert actual_msg == case_data[
#         "expected_result"], f"期望值: {case_data['expected_result']}, 实际值: {actual_msg}"
#
#     # 断言完成后，在个人信息页面点击返回按钮回到主页
#     ap.click_back_btn()
#     ip.click_back_btn()
