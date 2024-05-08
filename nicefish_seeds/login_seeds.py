import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class NicefishLoginSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def jump_from_home(self):
        # direct to the sign-in page from homepage
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/sign-in"]').click()
        print("direct to the sign-in page......")
        time.sleep(1)

    def execute_seeds(self, email="", password="12345678"):
        # in this step, we think our driver is at the sign-in page
        # input sign-in information
        print("start signing in......")

        signin_form = self.driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div/div[2]/form')
        # input email
        email_input = signin_form.find_element(By.CSS_SELECTOR, 'input[name="userName"]')
        email_input.clear()
        email_input.send_keys(email)
        # input password
        password_input = signin_form.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        password_input.clear()
        password_input.send_keys(password)  # password fixed
        # remember me
        remember_me = signin_form.find_element(By.CSS_SELECTOR, 'input[name="rememberMe"]')
        # randomly simulate the behavior of clicking the `remember me` button
        if random.randint(0,1) == 1:
            remember_me.click()
        # captcha
        captcha_input = signin_form.find_element(By.CSS_SELECTOR, 'input[name="captcha"]')
        # captcha in this website isn't valid, so we can input any content
        captcha_input.clear()
        captcha_input.send_keys("0")
        #
        submit_button = signin_form.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary me-3"]')
        submit_button.click()
        time.sleep(1)
        print("sign in success......")

