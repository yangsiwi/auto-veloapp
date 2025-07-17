import allure
import pytest
from utils.load_yaml import load_yaml
from page.bike_settings_page import BikeSettingsPage
from page.home_page import HomePage
from page.info_page import InfoPage


@allure.epic("velotric app应用")
@allure.story("个人信息模块")
class TestInfo:
    # 读取测试数据
    test_data = load_yaml('./data/home.yaml')

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("case_data", test_data,
                             ids=[f"{case['case_name']}" for case in test_data])
    def test_click_about_velotric(self, logged_in_driver, case_data):
        # 动态的标题
        allure.dynamic.title(f"{case_data['case_name']}")

        # 实例化 HomePage、InfoPage 对象
        hp = HomePage(logged_in_driver)
        ip = InfoPage(logged_in_driver)

        # 在首页点击"个人信息"按钮
        hp.click_userinfo()

        # 在个人信息页点击 "About Velotric" 按钮
        ip.click_about_velotric()

        # 断言是否成功进入ABOUT VELOTRIC页【判断进入到ABOUT VELOTRIC页面中是否有 "ABOUT VELOTRIC" 文字】
        actual_msg = ip.get_about_velotric_text()
        assert actual_msg == case_data[
            "expected_result"], f"期望值: {case_data['expected_result']}, 实际值: {actual_msg}"

        # 断言完成后，在个人信息页面点击返回按钮回到主页
        ip.click_back_btn()

        # 断言是否成功返回到首页【判断进入到首页页面中是否有 "START RIDING" 文字】
        # actual_msg = hp.click_start_riding()
        # assert actual_msg == case_data[
        #     "expected_result"], f"期望值: {case_data['expected_result']}, 实际值: {actual_msg}"

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize(
        "case_data",
        bike_settings_data,
        ids=[f"{case['case_name']}" for case in bike_settings_data]
    )
    def test_click_bike_settings(self, logged_in_driver, case_data):
        # 动态的标题
        allure.dynamic.title(f"{case_data['case_name']}")

        # 实例化 HomePage、BikeSettingsPage 对象
        hp = HomePage(logged_in_driver)
        bsp = BikeSettingsPage(logged_in_driver)

        # 在首页点击"车辆设置"按钮
        hp.click_bike_settings()

        # 断言是否成功进入车辆设置页【判断进入到车辆设置页面中是否有 "BIKE SETTINGS" 文字】
        actual_msg = hp.get_bike_settings_content_text()
        assert actual_msg == case_data["expected_result"], \
            f"期望值: {case_data['expected_result']}, 实际值: {actual_msg}"

        # 断言完成后，在车辆设置页面点击返回按钮回到首页
        bsp.click_back_btn()

        # 断言是否成功返回到首页【判断进入到首页页面中是否有 "START RIDING" 文字】
        # assert actual_msg == case_data[
        #     "expected_result"], f"期望值: {case_data['expected_result']}, 实际值: {actual_msg}"
