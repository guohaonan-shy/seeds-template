from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LakesideLogoutSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def execute_seeds(self):
        # input register information
        print("start logout......")
        # logout
        self.driver.find_element(By.XPATH, '//div[@class="right menu"]//a[@class="item"]').click()
        print("logout success......")