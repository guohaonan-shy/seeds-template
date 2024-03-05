from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Keys


class LakesideCompleteProfileSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def execute_seeds(self, first_name, last_name, street_address, postal_code, city, phone, birthday):
        # start completing user profile
        print("start completing profile......")
        # input first_name
        if first_name != "":
            first_name_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name=firstname]')
            first_name_input.clear()
            first_name_input.send_keys(first_name)
        # input last_name
        if last_name != "":
            last_name_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name=lastname]')
            last_name_input.clear()
            last_name_input.send_keys(last_name)
        # input street_address
        if street_address != "":
            street_address_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name=streetAddress]')
            street_address_input.clear()
            street_address_input.send_keys(street_address)
        # input postal_code
        if postal_code != "":
            postal_code_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="postalCode"]')
            postal_code_input.clear()
            postal_code_input.send_keys(postal_code)
        # input city
        if city != "":
            city_input = self.driver.find_element(By.CSS_SELECTOR, 'input[class="search"]')
            city_input.clear()
            city_input.send_keys(city)
        # input phone_number
        if phone != "":
            phone_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="phoneNumber"]')
            phone_input.clear()
            phone_input.send_keys(phone)

        # birthday
        if birthday != "":
            birthday_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="birthday"]')
            birthday_input.clear()
            dates = birthday.split("-")
            birthday_input.send_keys(dates[0])
            birthday_input.send_keys(Keys.RIGHT)
            birthday_input.send_keys(dates[1])
            birthday_input.send_keys(dates[2])
        # complete register
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="ui blue fluid button"]').click()
