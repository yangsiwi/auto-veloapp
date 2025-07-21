import allure

from base.keywords import Keywords
from locator.riding_locator import resume_btn

# 骑行页
class RidingPage(Keywords):

    @allure.step("点击暂停按钮")
    def click_resume_btn(self):
        self.click_element(resume_btn)


