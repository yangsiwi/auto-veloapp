from appium.webdriver.common.appiumby import AppiumBy

"""
个人信息页面的元素定位
"""

# 返回按钮
back_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)')

# 'My Rides' 卡片
my_rides_card = (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "My Rides")]')

# 'SETTINGS' 文案
SETTINGS_TEXT = (AppiumBy.XPATH, '//android.view.View[@content-desc="Settings"]')

# 'Account' 按钮
account_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Account"]')

# 'About Velotric' 按钮
about_velotric_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="About Velotric"]')
