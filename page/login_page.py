import time
import allure
from base.keywords import Keywords
from locator.login_locator import *


# 继承父类 用父类的点击输入方法  父类需要设备信息 传设备信息
class LoginPage(Keywords):

    # 登录的功能方法
    def login(self, username_text, password_text):
        try:
            # 强制等待
            time.sleep(5)
            # 输入用户邮箱
            with allure.step(f"输入用户邮箱：{username_text}"):
                # 点击邮箱输入框
                self.click_element(email_input)
                # 清空邮箱输入框
                self.clear_input(email_input)
                # 输入对应的用户邮箱
                self.input_element(email_input, username_text)
            # 输入用户密码
            with allure.step(f"输入用户密码：{password_text}"):
                # 点击密码输入框
                self.click_element(password_input)
                # 请空密码输入框
                self.clear_input(password_input)
                # 输入对应的用户密码
                self.input_element(password_input, password_text)
            # 点击登录
            with allure.step("点击登录"):
                # 收回系统内置键盘【部分机型如果不收回键盘，则找不到登录按钮】
                self.hide_keyboard()
                # 点击登录按钮
                self.click_element(Log_in_btn)
        except Exception as e:
            print("异常处理", e)

    # 登录成功的断言
    @allure.step("登录成功断言")
    def success_msg(self):
        sr_ele = self.wait_explicit(start_riding_ele)
        return sr_ele.get_attribute("content-desc")  # 获得文本

    # 登录失败的断言
    @allure.step("登录失败断言")
    def failed_msg(self):
        # 断言失败的函数
        error_message = self.wait_explicit(error_msg)
        return error_message.get_attribute("content-desc")
