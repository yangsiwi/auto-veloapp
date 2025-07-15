import allure
from selenium.webdriver.support.wait import WebDriverWait


# 项目中常用的操作 找到元素点击  找到元素输入  找元素 显示等待 等待 Keywords(driver)
class Keywords:
    # __init__ 只要实例化类就要传一个driver
    def __init__(self, driver):
        self.driver = driver

    # 显示等待元素 place (xx.id, 'xx')
    @allure.step("显示等待元素")
    def wait_explicit(self, place):
        ele = WebDriverWait(self.driver, 30).until(lambda x: x.find_element(*place))
        return ele

    # 找到元素点击
    @allure.step("点击元素")
    def click_element(self, place):
        try:
            self.wait_explicit(place).click()
        except Exception as e:
            print("异常处理")

    # 找到元素输入
    @allure.step("输入元素")
    def input_element(self, place, text):
        self.wait_explicit(place).send_keys(text)

    @allure.step("隐藏键盘")
    def hide_keyboard(self):
        if self.driver.is_keyboard_shown:
            self.driver.hide_keyboard()

    @allure.step("清空输入框")
    def clear_input(self, place):
        try:
            element = self.wait_explicit(place)
            element.clear()
        except Exception as e:
            print(f"清空失败: {e}")

