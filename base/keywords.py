import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


# 项目中常用的操作 找到元素点击  找到元素输入  找元素 显示等待 等待 Keywords(driver)
class Keywords:
    # __init__ 只要实例化类就要传一个driver
    def __init__(self, driver):
        self.driver = driver
        # 定义一个默认的超时时间，方便统一管理
        self.timeout = 30
        # 定义轮询周期
        self.poll_frequency = 0.5

    # --- 基础等待方法 ---
    @allure.step("等待元素出现")
    def wait_for_element_to_be_visible(self, locator):
        """
        等待元素在页面上可见。
        """
        try:
            return WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), f"等待元素 {locator} 可见超时",
                          allure.attachment_type.PNG)
            raise TimeoutException(f"等待元素 {locator} 可见超时")

    @allure.step("等待元素可被点击")
    def wait_for_element_to_be_clickable(self, locator):
        """
        等待元素可见并且可被点击。用于点击操作前，比单纯等待可见更可靠。
        """
        try:
            return WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), f"等待元素 {locator} 可点击超时",
                          allure.attachment_type.PNG)
            raise TimeoutException(f"等待元素 {locator} 可点击超时")

    # 显示等待元素 place (xx.id, 'xx')
    @allure.step("显示等待元素")
    def wait_explicit(self, place):
        ele = WebDriverWait(self.driver, 30).until(lambda x: x.find_element(*place))
        return ele

    # --- 核心操作方法 ---
    @allure.step("点击元素")
    def click_element(self, locator):
        """
        先等待元素可被点击，然后再执行点击操作。
        """
        element = self.wait_for_element_to_be_clickable(locator)
        element.click()

    @allure.step("输入文本")
    def input_text(self, locator, text):
        """
        先等待元素可见再输入。
        """
        element = self.wait_for_element_to_be_visible(locator)
        element.send_keys(text)

    @allure.step("清空并输入文本")
    def clear_and_input_text(self, locator, text):
        """
        将清空和输入两个操作合并，非常实用。
        """
        element = self.wait_for_element_to_be_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("获取元素属性")
    def get_element_attribute(self, locator, attribute_name):
        """
        封装获取元素属性的方法，避免在Page层写太多逻辑。
        """
        element = self.wait_for_element_to_be_visible(locator)
        return element.get_attribute(attribute_name)

    @allure.step("长按元素")
    def long_press_element(self, locator, duration_seconds=3):
        """
        使用 W3C Actions API 实现长按操作。
        :param locator: 元素定位器
        :param duration_seconds: 长按的持续时间（秒）
        """
        element = self.wait_for_element_to_be_visible(locator)

        # 1.创建一个指针输入源（模拟手指）
        finger = PointerInput("touch", "finger")

        # 2.创建一个动作序列
        actions = ActionChains(self.driver)

        # 3.定义动作：移动到元素中心 -> 按下手指 -> 等待指定时间 -> 松开手指
        actions.move_to_element(element)
        actions.pointer_down(button=PointerInput.MOUSE_BUTTON_LEFT)
        actions.pause(duration_seconds)
        actions.pointer_up(button=PointerInput.MOUSE_BUTTON_LEFT)

        # 4.执行动作
        actions.perform()

    @allure.step("隐藏键盘")
    def hide_keyboard(self):
        """
        判断键盘是否显示，如果显示则隐藏。
        """
        if self.driver.is_keyboard_shown:
            self.driver.hide_keyboard()

    # @allure.step("清空输入框")
    # def clear_input(self, place):
    #     try:
    #         element = self.wait_explicit(place)
    #         element.clear()
    #     except Exception as e:
    #         print(f"清空失败: {e}")

    # @allure.step("长按元素 {duration} 秒")
    # def long_press_element(self, place, duration=3):
    #     pass
