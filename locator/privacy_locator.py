from appium.webdriver.common.appiumby import AppiumBy

"""
PRIVACY POLICY 页面的元素定位
"""

# 返回按钮
back_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)')

# PRIVACY POLICY 顶部的文案
PRIVACY_POLICY_TEXT = (AppiumBy.XPATH, '//android.view.View[@content-desc="PRIVACY POLICY"]')
