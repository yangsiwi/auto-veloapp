from appium.webdriver.common.appiumby import AppiumBy

# 开始骑行按钮
start_riding_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="START RIDING"]')

# 车辆设置按钮
bike_settings_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="BIKE SETTINGS"]')

# 右上角个人信息图标
userinfo_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(1)')

