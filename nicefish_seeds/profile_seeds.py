import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class NicefishProfileSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def jump_to_profile(self):

        setting_button = self.driver.find_element(By.CSS_SELECTOR, 'a[class="nav-link"][href="/manage/chart"]')
        setting_button.click()
        time.sleep(2)
        print("direct to setting page......")

        profile_button = self.driver.find_element(By.CSS_SELECTOR, 'a[class="list-group-item"][href^="/manage/user-profile/"]')
        profile_button.click()
        time.sleep(2)
        print("direct to profile management......")

    def execute_seeds(self, avatar="", nickname="", remark="", password="12345678"):
        print("start editing the profile......")
        # upload avatar
        if avatar != "":
            file_upload = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="user.edit.plsUploadAvatar"]')
            abs_path = os.path.abspath(avatar)
            file_upload.send_keys(abs_path)
            time.sleep(1)  # waiting for uploading

        if nickname != "":
            nickname_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="nickName"]')
            nickname_input.clear()
            nickname_input.send_keys(nickname)

        if remark != "":
            remark_input = self.driver.find_element(By.CSS_SELECTOR, 'textarea[name="remark"]')
            remark_input.clear()
            remark_input.send_keys(remark)

        # have to fill in password
        password_input = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Please enter password."]')
        password_input.clear()
        password_input.send_keys(password)

        repeat_password_input = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Please enter repeat password."]')
        repeat_password_input.clear()
        repeat_password_input.send_keys(password)


        submit_button = self.driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary me-3"]')
        time.sleep(2)
        submit_button.click()
        time.sleep(2)
        print("submit......")


