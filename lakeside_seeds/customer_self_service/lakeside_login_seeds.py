import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LakesideLoginSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def execute_seeds(self, from_signup, email, password):

        if not from_signup:
            self.driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]').click()
            time.sleep(1)

        # input register information
        print("start login......")
        # input email
        email_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
        email_input.clear()
        email_input.send_keys(email)
        print(email_input.get_attribute("value"))
        # input password
        password_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        password_input.clear()
        password_input.send_keys(password)  # password fixed
        print(password_input.get_attribute("value"))
        # login
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="ui large fluid primary button"]').click()
        time.sleep(1)
        print("login success......")