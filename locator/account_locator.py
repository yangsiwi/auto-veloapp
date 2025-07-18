from appium.webdriver.common.appiumby import AppiumBy

"""
ACCOUNT 页面的元素定位
"""

# 顶部 'ACCOUNT' 文案
ACCOUNT_TEXT = (AppiumBy.XPATH, '//android.view.View[@content-desc="ACCOUNT"]')

# Change My Password 按钮
change_my_password = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Change My Password"]')

# Change My Email 按钮
change_my_email = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Change My Email"]')

# Delete My Account 按钮
delete_my_account = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Delete My Account"]')
