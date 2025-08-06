import allure
from selenium.common import TimeoutException

from base.keywords import Keywords
from locator.home_locator import *


# 车况页【用户首页】
class HomePage(Keywords):

    @allure.step("点击首页右上角个人信息按钮")
    def click_userinfo(self):
        self.click_element(userinfo_btn)

    @allure.step("点击开始骑行按钮")
    def click_start_riding(self):
        self.click_element(start_riding_btn)

    @allure.step("点击车辆设置按钮")
    def click_bike_settings(self):
        self.click_element(bike_settings_btn)

    @allure.step("在规定时间内获取蓝牙连接状态")
    def get_connection_status_text(self, timeout):
        """
        该方法检查蓝牙连接状态。
        它只负责返回页面的状态。

        1. 确认页面初始为 'Disconnected' 状态。
        2. 在指定的 `timeout` 时间内等待 'Connected' 文本出现。
        3. 如果成功等到，返回字符串 'true'。
        4. 如果超时，返回字符串 'false'。

        :param timeout: 从 yaml 文件中读取的自定义超时时间（秒）。
        :return: 字符串 'true' 或 'false'。
        """
        try:
            # 确认初始状态是 '未连接'
            allure.attach("检查点: 确认 'Disconnected' 状态存在。", name="初始状态检查")
            self.wait_for_element_to_be_visible(disconnected_text, timeout=10)

            # 核心等待逻辑：等待 '已连接' 状态出现
            allure.attach(f"核心等待: 等待 'Connected' 状态出现，最长 {timeout} 秒。", name="等待连接")
            self.wait_for_element_to_be_visible(connected_text, timeout=timeout)

            # 如果等到，说明连接成功，返回 'true'
            allure.attach("状态获取成功：'Connected' 文本已出现。", name="成功状态")
            return "true"

        except TimeoutException:
            # 如果在指定的timeout时间内，'CONNECTED' 元素没有出现，则捕获此异常
            allure.attach(f"状态获取失败：在 {timeout} 秒内未等到 'Connected' 文本。", name="失败状态")
            allure.attach(self.driver.get_screenshot_as_png(), "连接超时截图", allure.attachment_type.PNG)
            return "false"
        except Exception as e:
            # 捕获其他可能发生的未知异常
            allure.attach(f"获取状态时发生未知错误: {e}", name="未知错误")
            allure.attach(self.driver.get_screenshot_as_png(), "错误截图", allure.attachment_type.PNG)
            return "false"