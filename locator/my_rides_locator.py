from appium.webdriver.common.appiumby import AppiumBy

# 'MY RIDES' 文案
MY_RIDES_TEXT = (AppiumBy.XPATH, '//android.view.View[@content-desc="MY RIDES"]')

# Day 按钮
day_tab_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Day"]')

# Week 按钮
week_tab_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Week"]')

# Month 按钮
month_tab_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Month"]')

# Year 按钮
year_tab_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Year"]')
