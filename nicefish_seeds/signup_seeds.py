import random

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class NicefishSignUpSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def execute_seeds(self, email="TestUser{}".format(random.randint(0, 10000)), password="123456"):
        # signup in homepage
        signup = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/sign-up"]')
        signup.click()

        # input register information
        print("start signing up......")

        signup_form = self.driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div/div[2]/form')
        # input email
        email_input = signup_form.find_element(By.CSS_SELECTOR, 'input[name="email"]')
        email_input.clear()
        email_input.send_keys(email)
        # input password
        password_input = signup_form.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        password_input.clear()
        password_input.send_keys(password)  # password fixed
        # confirm password again
        password_confirm_input = signup_form.find_element(By.CSS_SELECTOR, 'input[name="confirmPassword"]')
        password_confirm_input.clear()
        password_confirm_input.send_keys(password)  # password fixed
        # sign up
        signup_form.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]').click()
        print("signup success......")