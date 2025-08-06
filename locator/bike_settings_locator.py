from appium.webdriver.common.appiumby import AppiumBy

# BIKE SETTINGS 文案
BIKE_SETTINGS_TEXT = (AppiumBy.XPATH, '//android.view.View[@content-desc="BIKE SETTINGS"]')

# 返回按钮
back_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)')

# --- 车辆名称相关元素 ---
# 车辆名元素【先点击车辆名元素，弹出车辆名修改输入框】
edit_bike_name = (AppiumBy.XPATH, '//android.widget.ImageView[1]')
# 车辆名弹窗输入框
bike_name_input = (AppiumBy.XPATH, '//android.widget.EditText')
# 车辆名弹窗的确定按钮
bike_name_confirm_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Confirm"]')
# 车辆名弹窗的取消按钮
bike_name_cancel_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Cancel"]')
# 车辆名弹窗的x按钮【x按钮是一键清空输入框中的内容】
bike_name_clear_btn = (AppiumBy.XPATH, '//android.widget.ImageView')

# --- Riding Mode相关元素 ---
# Eco Mode 元素【点击之后会弹出NOTICE框，点击 Confirm 按钮才会切换到 Eco 模式】
eco_mode_btn = (AppiumBy.XPATH, '//android.widget.ImageView[2]')
# Trail Mode 元素【点击之后会弹出NOTICE框，点击 Confirm 按钮才会切换到 Trail 模式】
trail_mode_btn = (AppiumBy.XPATH, '//android.widget.ImageView[3]')
# Boost Mode 元素【点击之后会弹出NOTICE框，点击 Confirm 按钮才会切换到 Boost 模式】
boost_mode_btn = (AppiumBy.XPATH, '//android.widget.ImageView[4]')
# Riding Mode的确认框
mode_confirm_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Confirm"]')
# # Riding Mode的取消框
mode_cancel_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Cancel"]')

# Screen Brightness
screen_brightness_btn_1 = (AppiumBy.XPATH, '//android.view.View[@content-desc="1"]')
screen_brightness_btn_2 = (AppiumBy.XPATH, '//android.view.View[@content-desc="2"]')
screen_brightness_btn_3 = (AppiumBy.XPATH, '//android.view.View[@content-desc="3"]')
screen_brightness_btn_4 = (AppiumBy.XPATH, '//android.view.View[@content-desc="4"]')
screen_brightness_btn_5 = (AppiumBy.XPATH, '//android.view.View[@content-desc="5"]')
screen_brightness_btn_auto = (AppiumBy.XPATH, '//android.view.View[@content-desc="Auto"]')
