# import allure
# import pytest
#
# from utils.load_yaml import load_yaml
#
#
# @allure.epic("velotric app应用")
# @allure.story("账户模块")
# class TestAccount:
#     # 加载所有数据
#     all_info_data = load_yaml('./data/info.yaml')
#
#     # 创建一个 Page Object 的映射字典
#     # 键是 YAML 中的字符串，值是真正的页面类
#     PAGE_OBJECTS = {
#         'InfoPage': InfoPage,
#         'MyRidesPage': MyRidesPage,
#         'AccountPage': AccountPage,
#         'AboutPage': AboutPage,
#         'DataSyncPage': DataSyncPage,
#         'HelpPage': HelpPage
#     }
#
#     LOCATORS = {
#         'kilometers_btn': kilometers_btn,
#         'miles_btn': miles_btn,
#         'app_version_toast': app_version_toast,
#     }
#
#
#     @pytest.mark.run(order=4)
#     @pytest.mark.parametrize("case", all_info_data, ids=[f"{case['case_name']}" for case in all_info_data])
#    def test_navigation(self)
#