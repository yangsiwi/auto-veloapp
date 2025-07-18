import allure
import pytest

from conftest import info_page_setup
from page.about_page import AboutPage
from page.account_page import AccountPage
from page.my_rides_page import MyRidesPage
from utils.load_yaml import load_yaml
from page.home_page import HomePage
from page.info_page import InfoPage


@allure.epic("velotric app应用")
@allure.story("个人信息模块")
class TestInfo:
    # 1.加载所有数据
    all_subpage_data = load_yaml('./data/info.yaml')

    # 2.将所有场景的数据合并到一个列表中，用于参数化
    # all_subpage_data = (
    #         test_data['my_rides_data'] +
    #         test_data['account_data'] +
    #         test_data['about_velotric_data']
    # )

    # 3.创建一个 Page Object 的映射字典
    # 键是 YAML 中的字符串，值是真正的页面类
    PAGE_OBJECTS = {
        'MyRidesPage': MyRidesPage,
        'AccountPage': AccountPage,
        'AboutPage': AboutPage
    }

    # 4.使用合并后的数据进行参数化
    @pytest.mark.parametrize("case", all_subpage_data, ids=[f"{case['case_name']}" for case in all_subpage_data])
    def test_subpage_navigation(self, info_page_setup, case):
        """
        【通用引擎】测试从个人信息页到子页面的导航和返回
        """
        allure.dynamic.title(case['case_name'])

        # --- Setup ---
        # 从 fixture 直接解包获取 driver 和已经实例化好的 ip 对象
        driver, ip = info_page_setup

        # 从YAML获取需要实例化的页面类名，并通过字典找到对应的类
        NextPageClass = self.PAGE_OBJECTS[case['page_object_name']]
        # 实例化目标页面对象
        next_page = NextPageClass(driver)

        with allure.step(f"{case['case_name']}的目标链接"):
            # 【核心】使用getattr 动态调用 InfoPage上面的点击方法
            info_page_click_method = getattr(ip, case['click_method'])
            info_page_click_method()

        with allure.step("断言是否成功进入到子页面"):
            # 【核心】使用 getattr 动态调用目标页面上的验证方法
            next_page_verify_method = getattr(next_page, case['verify_method'])
            actual_msg = next_page_verify_method()
            assert actual_msg == case['expected_result'], f"期望值: {case['expected_result']}, 实际值: {actual_msg}"

        with allure.step("逐层返回，恢复App到主页状态"):
            # 【核心】next_page是动态的，但是back_btn方法是所有子页面共有的
            next_page.click_back_btn()


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
