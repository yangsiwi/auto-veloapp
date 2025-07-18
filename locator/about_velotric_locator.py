from appium.webdriver.common.appiumby import AppiumBy

"""
ABOUT VELOTRIC 页面的元素定位
"""

# 顶部 'ABOUT VELOTRIC' 文案
ABOUT_VELOTRIC_TEXT = (AppiumBy.XPATH, '//android.view.View[@content-desc="ABOUT VELOTRIC"]')

# Terms of Use 按钮
terms_of_use = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Terms of Use"]')

# Privacy Policy 按钮
privacy_policy = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Privacy Policy"]')
