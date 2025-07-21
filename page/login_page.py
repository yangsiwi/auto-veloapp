import allure
from base.keywords import Keywords
from locator.login_locator import *

# 登录页
class LoginPage(Keywords):

    # 登录的功能方法
    def login(self, email_text, password_text):
        # 输入用户邮箱
        with allure.step(f"输入用户邮箱：{email_text}"):
            self.click_element(email_input)
            self.clear_and_input_text(email_input, email_text)
        # 输入用户密码
        with allure.step(f"输入用户密码：{password_text}"):
            self.click_element(password_input)
            self.clear_and_input_text(password_input, password_text)
        # 点击登录
        with allure.step("点击登录"):
            # 收回系统内置键盘【部分机型如果不收回键盘，则找不到登录按钮】
            self.hide_keyboard()
            # 点击登录按钮
            self.click_element(Log_in_btn)

    @allure.step("获取登录成功信息")
    def get_success_message(self):
        return self.get_element_attribute(start_riding_ele, "content-desc")

    @allure.step("获取登录失败信息")
    def get_failed_message(self):
        return self.get_element_attribute(error_msg, "content-desc")
