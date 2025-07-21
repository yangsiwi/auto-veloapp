import time

import allure
import pytest


# 这个函数现在是全局可用的
def run_navigation_test(driver, start_page_object, case_data, page_object_map):
    """
    一个通用的、可复用的子页面导航测试流程。

    :param driver: WebDriver 实例。
    :param start_page_object: 测试流程的起始页面对象实例 (例如 InfoPage() 的实例)。
    :param case_data: 从YAML加载的单条测试用例数据。
    :param page_object_map: 一个页面类名字典，用于查找目标页面的类。
    """
    with allure.step(f"执行点击: {case_data['click_method']}"):
        # 在【起始页面】上，动态调用点击方法
        click_method_on_start_page = getattr(start_page_object, case_data['click_method'])
        click_method_on_start_page()

    # 从字典中找到目标页面的【类】
    NextPageClass = page_object_map[case_data['page_object_name']]
    # 实例化目标页面的【对象】
    next_page = NextPageClass(driver)

    with allure.step(f"断言页面标题为: '{case_data['expected_result']}'"):
        # 在【目标页面】上，动态调用验证方法
        verify_method_on_next_page = getattr(next_page, case_data['verify_method'])
        actual_msg = verify_method_on_next_page()
        assert actual_msg == case_data['expected_result'], "页面标题断言失败"

    with allure.step("返回到上一页"):
        time.sleep(2)
        # 假设所有子页面都有一个 click_back_btn 方法
        next_page.click_back_btn()
