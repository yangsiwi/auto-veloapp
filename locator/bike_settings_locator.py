from appium.webdriver.common.appiumby import AppiumBy


# BIKE SETTINGS 文案
BIKE_SETTINGS_TEXT = (AppiumBy.XPATH, '//android.view.View[@content-desc="BIKE SETTINGS"]')

# 返回按钮
back_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)')

# Eco Mode
eco_mode_btn = (AppiumBy.ID,
                '//android.widget.ImageView[@content-desc="Eco Mode\nExtends battery life, providing optimal efficiency for longer rides."')

# Trail Mode
trail_mode_btn = (AppiumBy.ID, '//android.widget.ImageView[@content-desc="Trail Mode\nTackles diverse terrains balancing energy efficiency and power seamlessly."]')

# Boost Mode
boost_mode_btn = (AppiumBy.ID, '//android.widget.ImageView[@content-desc="Boost Mode\nOffers maximum assistance for steep climbs and challenging inclines"]')


