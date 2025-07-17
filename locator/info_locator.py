from appium.webdriver.common.appiumby import AppiumBy

# user_email = (AppiumBy.XPATH, '//android.view.View[matches(@content-desc, "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")]')
# user_email = (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "@")]')

# 'SETTINGS' 文案
SETTINGS_TEXT = (AppiumBy.XPATH, '//android.view.View[@content-desc="Settings"]')

# 返回按钮
back_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)')

# About Velotric 按钮
about_velotric_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="About Velotric"]')