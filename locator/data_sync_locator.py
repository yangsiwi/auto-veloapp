
"""
DATA SYNCHRONIZATION 页面的元素定位
"""
from appium.webdriver.common.appiumby import AppiumBy

# 顶部 'DATA SYNCHRONIZATION' 文案
DATA_SYNCHRONIZATION_TEXT = (AppiumBy.XPATH, '//android.view.View[@content-desc="DATA SYNCHRONIZATION"]')

# Health Connect 按钮
health_connect_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Health Connect"]')