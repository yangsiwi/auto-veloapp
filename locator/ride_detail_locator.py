from appium.webdriver.common.appiumby import AppiumBy

"""
骑行记录卡片详情页面的元素定位
"""

# 返回按钮
back_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)')

share_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Share"]')