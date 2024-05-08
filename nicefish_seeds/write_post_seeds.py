import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class NicefishWritePostSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def jump_to_write_post(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/write"]').click()
        time.sleep(2)

    def execute_seeds(self, material_path="/", description=""):
        # at this stage, we have posited in the post-editing page
        print("start editing the post......")
        # upload image or video
        file_upload = self.driver.find_element(By.CSS_SELECTOR, 'input[accept="image/*,video/mp4"]')
        abs_path = os.path.abspath(material_path)
        file_upload.send_keys(abs_path)
        time.sleep(1)  # waiting for uploading
        # form
        form = self.driver.find_element(By.CSS_SELECTOR, 'form[role="form"]')
        # input the description
        content_input = form.find_element(By.CSS_SELECTOR, 'textarea[name="content"]')
        content_input.clear()
        content_input.send_keys(description)
        # input the captcha
        captcha_input = form.find_element(By.CSS_SELECTOR, 'input[name="captcha"]')
        captcha_input.send_keys("0")
        time.sleep(2)
        # submit
        submit_button = form.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
        submit_button.click()
        print("edit post success......")
        time.sleep(2)
