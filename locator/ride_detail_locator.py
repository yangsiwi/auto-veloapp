from appium.webdriver.common.appiumby import AppiumBy

"""
骑行记录卡片详情页面的元素定位
"""

# 返回按钮
back_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(6)')

# 地图
map_locator = (AppiumBy.XPATH,
               '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.FrameLayout')

# Share分享按钮
share_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Share"]')
