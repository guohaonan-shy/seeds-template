import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LakesideChangeAddressSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def execute_seeds(self, street_address, postal_code, city):
        change_address_button = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/profile/change-address"]')
        change_address_button.click()
        time.sleep(1)
        print("start changing address......")
        # input street_address
        if street_address != "":
            street_address_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="streetAddress"]')
            street_address_input.clear()
            street_address_input.send_keys(street_address)
        # input postal_code
        if postal_code != "":
            postal_code_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="postalCode"]')
            postal_code_input.clear()
            postal_code_input.send_keys(postal_code)
        # input city
        if city != "":
            city_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
            city_input.clear()
            city_input.send_keys(city)

        save_changes_button = self.driver.find_element(By.CSS_SELECTOR, 'button[class="ui blue fluid button"]')
        save_changes_button.click()
        time.sleep(1)
        # jump back to the profile tab

    def jump_to_profile(self):

        if self.driver.current_url == "http://localhost:3000/profile":
            return

        if self.driver.current_url == "http://localhost:3000/policies" or "http://localhost:3000/contact":
            profile_tab = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/profile"]')
            profile_tab.click()
            time.sleep(1)
            return

        print("call panic")
