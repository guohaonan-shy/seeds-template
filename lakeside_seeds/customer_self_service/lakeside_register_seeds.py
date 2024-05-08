import random

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LakesideRegisterNewUserSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def execute_seeds(self, email="testUser{}".format(random.randint(0, 10000)), password="123456"):
        # signup in homepage
        signup = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/signup"]')
        signup.click()

        # input register information
        print("start register......")
        # input email
        email_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name=email]')
        email_input.clear()
        email_input.send_keys(email)
        # input password
        password_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name=password]')
        password_input.clear()
        password_input.send_keys(password)  # password fixed
        # agree to terms and conditions
        self.driver.find_element(By.CSS_SELECTOR, 'div[class="ui checkbox"]').click()
        # sign up
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="ui large fluid primary button"]').click()
        print("register success......")