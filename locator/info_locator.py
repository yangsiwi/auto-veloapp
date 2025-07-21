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

# 'Data Synchronization' 按钮
data_synchronization_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Data Synchronization"]')

# 'About Velotric' 按钮
about_velotric_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="About Velotric"]')

# 'Help' 按钮
help_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Help"]')

# 'Unit' 按钮
unit_btn = (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "Unit")]')

# 底部弹窗中的 "Miles(mi)" 按钮
miles_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Miles (mi)"]')

# 底部弹窗中的 "Kilometers(km)" 按钮
kilometers_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Kilometers (km)"]')

# 'App Version' 按钮
app_version_btn = (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "App Version")]')

# 【新】为 "App Version" 的 "No update available" 提示添加专用定位器
# 我们用 content-desc 来精确定位
app_version_toast = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="No update available"]')