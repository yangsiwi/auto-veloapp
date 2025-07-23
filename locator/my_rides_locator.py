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

# 定位【所有】骑行记录卡片的通用 XPath
# 我们通过 content-desc 包含 "AM" 或 "PM" 来识别它们
RIDE_CARD_ITEMS = (AppiumBy.XPATH,
                   '//android.widget.ScrollView//android.view.View[contains(@content-desc, " AM") or contains(@content-desc, " PM")]')

# 定位【最后一个】骑行记录卡片的 XPath
LAST_RIDE_CARD_ITEM = (AppiumBy.XPATH,
                       '(//android.widget.ScrollView//android.view.View[contains(@content-desc, " AM") or contains(@content-desc, " PM")])[last()]')
