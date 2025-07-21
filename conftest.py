import time
import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from locator.login_locator import sign_btn
from page.about_page import AboutPage
from page.home_page import HomePage
from page.info_page import InfoPage
from page.login_page import LoginPage
from utils.load_yaml import load_yaml


@pytest.fixture(scope='session')
def get_driver_options():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "14"
    options.device_name = "R3CT90HL0QB"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.mddoscar.velotricbike"
    options.app_activity = "com.example.velotric_app.MainActivity"
    options.auto_grant_permissions = True
    # options.no_reset = True # 在调试或需要保持状态时可以取消注释
    return options


@pytest.fixture(scope='session')
def app_setup(request, get_driver_options):
    # setup 部分: 在整个测试会话开始时运行一次
    print("\n[Session Setup] : 启动Appium Driver...")

    # 从 get_driver_options 获取配置
    driver = webdriver.Remote("http://127.0.0.1:4723", options=get_driver_options)

    # 使用 request.addfinalizer 来注册清理函数，这是 session 级别推荐的做法
    def finalizer():
        print("\n[Session Teardown] : 关闭Appium Driver。")
        driver.quit()

    request.addfinalizer(finalizer)
    return driver  # 直接返回 driver


@pytest.fixture(scope='session')
def logged_in_driver(app_setup):
    driver = app_setup
    if not getattr(driver, "is_logged_in", False):
        print("\n[Session Setup] : 执行前置登录...")
        login_page = LoginPage(driver)

        # 等待app启动稳定
        time.sleep(3)

        try:
            login_page.click_element(sign_btn)
        except Exception as e:
            pytest.fail(f"会话级登录失败: 无法点击 'Sign in' 按钮。错误: {e}")

        all_test_data = load_yaml("data/login.yaml")
        success_case_data = next((case for case in all_test_data if case.get("case_id") == "login003"), None)

        # 【修正】修复缩进，这个if块应该独立
        if not success_case_data:
            pytest.fail("在 login.yaml 中未找到 case_id 为 'login003' 的成功登录用例数据。")

        # 【修正】这部分代码应该在 if 之外，确保总能被执行
        params = success_case_data['all_params']
        username = params['username']
        password = params['password']

        allure.step(f"执行会话级前置登录，用户: {username}")
        login_page.login(username, password)

        try:
            login_page.get_success_message()
            allure.step("会话级前置登录成功，已进入应用主页。")
            driver.is_logged_in = True
        except Exception:
            allure.attach(driver.get_screenshot_as_png(), "会话级前置登录失败截图", allure.attachment_type.PNG)
            pytest.fail(f"会話级前置登录失败，用户: {username}。测试无法继续。")

    return driver


# 为登录测试模块专用的、函数级别的 fixture
@pytest.fixture(scope='function')
def login_test_driver(request, get_driver_options):
    print("\n[Function Setup for Login Test] : 启动独立的Driver...")
    driver = webdriver.Remote("http://127.0.0.1:4723", options=get_driver_options)

    # 等待app启动稳定
    time.sleep(3)

    try:
        driver.find_element(*sign_btn).click()
    except Exception as e:
        pytest.fail(f"登录测试启动失败: 无法点击 'Sign in' 按钮。错误: {e}")

    yield driver

    print("\n[Function Teardown for Login Test] : 关闭独立的Driver。")
    driver.quit()

@pytest.fixture(scope='module')
def info_page_setup(logged_in_driver):
    """
    一个专门为个人信息模块测试准备的 fixture。
    它会确保测试开始时，App已经位于个人信息页面。
    """
    print("\n[Module Setup for Info Test] : 导航到个人信息页...")
    hp = HomePage(logged_in_driver)
    hp.click_userinfo()

    # 将 driver 和 InfoPage 实例一同传递给测试用例
    yield logged_in_driver, InfoPage(logged_in_driver)

    # teardown: 在模块所有用例结束后，点击一次返回，回到主页
    print("\n[Module Teardown for Info Test] : 从个人信息页返回主页。")
    InfoPage(logged_in_driver).click_back_btn()

@pytest.fixture(scope='module')
def about_page_setup(logged_in_driver):
    """
    一个专门为关于模块测试准备的 fixture。
    它会确保测试开始时，App已经位于关于信息页面。
    """
    print("\n[Module Setup for Info Test] : 导航到关于页...")

    hp = HomePage(logged_in_driver)
    hp.click_userinfo()
    ip = InfoPage(logged_in_driver)
    ip.click_about_velotric()

    # 将 driver 和 AboutPage 实例一同传递给测试用例
    yield logged_in_driver, AboutPage(logged_in_driver)

    # teardown: 在模块所有用例结束后，点击一次返回，回到主页
    print("\n[Module Teardown for Info Test] : 从关于信息页返回主页。")
    AboutPage(logged_in_driver).click_back_btn()
    InfoPage(logged_in_driver).click_back_btn()

# 钩子函数 作用：在测试用例执行后（无论成功/失败）自动截图添加到allure报告中
# tryfirst 确保钩子优先执行
# hookwrapper 可以获取到测试执行的最终结果
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    钩子函数，在每个测试用例执行完毕后（无论成功或失败）自动截图。
    """

    # 这一行是固定的模板代码，它会先去执行测试用例，
    # 然后再回到这里，并将测试结果封装在 outcome 对象中。
    outcome = yield  # 暂停执行，等待用例完成

    # 从 outcome 中获取详细的测试报告对象
    report = outcome.get_result()

    # 我们只关心测试用例的核心执行阶段（'call'阶段），
    # 并且现在我们希望无论是成功(passed)还是失败(failed)都执行后续操作。
    if report.when == "call" and (report.failed or report.passed):
        # --- 智能获取 driver 的核心代码 ---
        # item.funcargs 是一个字典，包含了该测试用例所使用的所有 fixture 的实例。
        # 我们尝试从中获取 'logged_in_driver'，如果不存在，再尝试获取 'app_setup'。
        # 这种写法可以确保无论用例传入哪个 fixture，都能拿到 driver。
        driver = item.funcargs.get("logged_in_driver") or item.funcargs.get("app_setup")

        # 如果成功获取到了 driver 实例
        if driver:
            try:
                # --- 统一截图逻辑 ---
                # 根据测试结果（成功或失败）决定截图的标题
                status = "成功" if report.passed else "失败"
                step_title = f"添加{status}截图"
                screenshot_name = f"{status}截图"

                # 使用 allure.step 来组织报告，让截图在报告中更清晰
                with allure.step(step_title):
                    # 获取截图的二进制数据，并附加到 Allure 报告中
                    allure.attach(
                        driver.get_screenshot_as_png(),
                        name=screenshot_name,
                        attachment_type=allure.attachment_type.PNG
                    )
            except Exception as e:
                # 增加一个异常处理，防止因截图失败（如driver已关闭）导致报告系统本身出错
                print(f"警告：为用例 {item.name} 截图失败，错误信息: {e}")

            # # 截图
            # if report.failed:
            #     with allure.step("添加失败的截图"):
            #         allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
            # elif report.passed:
            #     with allure.step("添加成功的截图"):
            #         allure.attach(driver.get_screenshot_as_png(), "成功截图", allure.attachment_type.PNG)
