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
error_msg = (AppiumBy.XPATH, '//android.widget.ImageView[string-length(@content-desc) > 0]')
