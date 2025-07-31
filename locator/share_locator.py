
"""
SHARE MY RIDE 页面的元素定位
"""
from appium.webdriver.common.appiumby import AppiumBy

# 返回按钮
back_btn = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(4)')

# SHARE MY RIDE 文案
SHARE_MY_RIDE_TEXT = (AppiumBy.XPATH, '//android.view.View[@content-desc="SHARE MY RIDE"]')

# Share 按钮
share_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Share"]')

# 骑行记录卡片
ride_card = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ImageView").instance(0)')

# 点击 Share 按钮后弹出的系统弹窗中的 "更多" 按钮文案
MORE_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("更多")')

# Add image 按钮
add_image_btn = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Add image"]')

# 点击 Add image 按钮后底部弹窗中的文案
# Take Photo

TAKE_PHOTO_TEXT = (AppiumBy.XPATH, '//android.view.View[@content-desc="Take photo"]')

# Select from Gallery
SELECT_FROM_GALLERY_TEXT = (AppiumBy.XPATH, '//android.view.View[@content-desc="Select from gallery"]')

# cancel_btn
cancel_btn = (AppiumBy.XPATH, '//android.view.View[@content-desc="Cancel"]')