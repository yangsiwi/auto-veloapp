import time
import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from locator.login_locator import sign_btn


@pytest.fixture(scope='function')
# function每次启动一次设备信息
# session 一次设备信息打开用例全运行完在关闭
def login_driver(request):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "14"
    options.device_name = "R3CT90HL0QB"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.mddoscar.velotricbike"
    options.app_activity = "com.example.velotric_app.MainActivity"
    options.auto_grant_permissions = True
    # options.no_reset = True

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    time.sleep(2)

    # 点击 Sign 按钮
    driver.find_element(*sign_btn).click()

    yield driver

    time.sleep(3)

    def end():
        driver.press_keycode(3)  # 模拟按下手机的HOME键  退出当前的应用

    request.addfinalizer(end)  # 即使测试的时候抛出了异常也会执行退出清理的操作


# 普通函数用函数 调用 函数名() 能拿到返回值
# conftest+fixture  函数名  能拿到返回值  yield 表示这个fixture提供一个driver对象给用例使用
# 流程
# 1.先执行yield之前的数据
# 2.yield 暂停 把driver传给用例（test_login）
# 3.执行test_login用例
# 4.yield之后的代码 关闭设备
# yield 执行流程
# 用例执行前，执行yield之前的代码
# 将driver对象传给用例，用例执行
# 用例执行完后，回到fixture执行yield后面的代码

# 钩子函数  固定 作用：在测试用例执行后（无论成功/失败）自动截图添加到allure报告中
# tryfirst 确保钩子优先执行
# hookwrapper 可以获取到测试执行的最终结果
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield  # 暂停执行，等待用例完成
    report = outcome.get_result()  # 获取测试结果
    # 执行测试阶段和关注成功或者失败的状态
    if report.when == "call" and (report.failed or report.passed):
        # 从conftest中拿设备信息
        driver = item.funcargs.get("login_driver")
        # 相当于  driver=Context.driver
        # driver=getattr(Context,"driver")#从全局中拿到我们的值
        if driver:
            # 截图
            if report.failed:
                with allure.step("添加失败的截图"):
                    allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
            elif report.passed:
                with allure.step("添加成功的截图"):
                    allure.attach(driver.get_screenshot_as_png(), "成功截图", allure.attachment_type.PNG)
