# Health Connect Locator
from appium.webdriver.common.appiumby import AppiumBy

# 返回按钮
back_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)')

# 顶部文案 【SYNCHRONIZE WITH ANDROID】
SYNC_WITH_ANDROID_TEXT = (AppiumBy.XPATH, '//android.view.View[@content-desc="SYNCHRONIZE WITH ANDROID"]')

# Connect 按钮
connect_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Connect"]')

# 全部允许按钮
allow_all_btn = (AppiumBy.XPATH, '//android.widget.Switch[@resource-id="android:id/switch_widget"]')

# 底部允许按钮
allow_btn = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.healthconnect.controller:id/primary_button_outline"]')

# Health Connect 元素【右侧显示 Connect 或 Disconnect】
health_connect = (AppiumBy.XPATH, '//android.widget.ImageView[starts-with(@content-desc, "Health Connect")]')

# Auto Sync 按钮
auto_sync_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Switch")')