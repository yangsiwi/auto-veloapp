# 登录页面的定位
from appium.webdriver.common.appiumby import AppiumBy

# Sign 按钮
sign_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Sign in"]')

# Email 输入框
email_input = (AppiumBy.XPATH, '//android.widget.EditText[@hint="Email"]')

# Password 输入框
password_input = (AppiumBy.XPATH, '//android.widget.EditText[@hint="Password"]')

# Log in按钮
Log_in_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Log in"]')

# ===========================================================================================

# 断言 首页的开始骑行按钮
start_riding_ele = (AppiumBy.XPATH, '//android.view.View[@content-desc="START RIDING"]')

# 断言 登录的错误信息
# error_msg = (AppiumBy.XPATH, '//android.widget.ImageView[string-length(@content-desc) > 0]')
# 【优化】断言登录的错误信息
# 这个定位器现在有两个作用：
# 1. 获取 content-desc 来断言错误文本是否正确。
# 2. 定位这个全屏的ImageView元素，以便我们能等待它消失。
error_msg = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc and string-length(@content-desc) > 0]')

# 【新增】Toast 错误提示弹窗的定位器
# 它会匹配任何包含关键错误文本的元素。
# 注意：安卓的Toast的text属性可能需要用@text来获取，请用Appium Inspector确认。
# toast_error_element = (AppiumBy.XPATH, "//*[contains(@text, 'User Missing') or contains(@text, 'Wrong email address or password')]")
