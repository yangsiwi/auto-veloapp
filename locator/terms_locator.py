from appium.webdriver.common.appiumby import AppiumBy

"""
TERMS OF USE 页面的元素定位
"""

# 返回按钮
back_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)')

# TERMS OF USE 顶部的文案
TERMS_OF_USE_TEXT = (AppiumBy.XPATH, '//android.view.View[@content-desc="TERMS OF USE"]')
