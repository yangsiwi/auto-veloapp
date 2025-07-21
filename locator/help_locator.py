"""
HELP 页面的元素定位
"""
from appium.webdriver.common.appiumby import AppiumBy

# 顶部 'HELP' 文案
HELP_TEXT = (AppiumBy.XPATH, '//android.view.View[@content-desc="HELP"]')

# FAQ 按钮
faq_btn = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="FAQ"]')

# Feedback 按钮
feedback_btn = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Feedback"]')

# Part Replacement 按钮
part_replacement_btn = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Part Replacement"]')