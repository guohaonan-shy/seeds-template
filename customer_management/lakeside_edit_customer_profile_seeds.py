import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LakesideEditCustomerProfileSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        pass

    def execute_seeds(self, first_name: str, last_name: str, date_of_birth: str, street_address: str, postal_code: str,
                      city: str, email_address: str, phone_number: str):

        print("click 'Edit' button")
        edit = self.driver.find_element(By.XPATH, ".//a[@class='ui mini basic compact right floated button']")
        edit.click()

        form = self.driver.find_element(By.XPATH, ".//form[@class='ui form']")

        # first name
        first_name_input = form.find_element(By.XPATH, ".//input[@name='firstname']")
        if first_name != "":
            first_name_input.clear()
            first_name_input.send_keys(first_name)
            print(first_name_input.get_attribute("value"))
        # last name
        last_name_input = form.find_element(By.XPATH, ".//input[@name='lastname']")
        if last_name != "":
            last_name_input.clear()
            last_name_input.send_keys(last_name)
            print(last_name_input.get_attribute("value"))
        # date_of_birth
        date_input = form.find_element(By.XPATH, ".//input[@name='birthday']")
        if date_of_birth != "":
            date_input.clear()
            dates = date_of_birth.split("-")
            date_input.send_keys(dates[0])
            date_input.send_keys(Keys.RIGHT)
            date_input.send_keys(dates[1])
            # date_input.send_keys(Keys.RIGHT)
            date_input.send_keys(dates[2])
            # self.driver.execute_script("arguments[0].value = '1998-04-21';", date_input)
            # date_input.send_keys(date_of_birth)
            print(date_input.get_attribute("value"))
        # street_address
        address_input = form.find_element(By.XPATH, ".//input[@name='streetAddress']")
        if street_address != "":
            address_input.clear()
            address_input.send_keys(street_address)
            print(address_input.get_attribute("value"))
        # postal_code
        postal_code_input = form.find_element(By.XPATH, ".//input[@name='postalCode']")
        if postal_code != "":
            postal_code_input.clear()
            postal_code_input.send_keys(postal_code)
            print(postal_code_input.get_attribute("value"))
        # city
        city_input = form.find_element(By.XPATH, ".//input[@name='city']")
        if city != "":
            city_input.clear()
            city_input.send_keys(city)
            print(city_input.get_attribute("value"))
        # email_address
        email_input = form.find_element(By.XPATH, ".//input[@name='email']")
        if email_address != "":
            email_input.clear()
            email_input.send_keys(email_address)
            print(email_input.get_attribute("value"))
        # phone_number
        phone_input = form.find_element(By.XPATH, ".//input[@name='phoneNumber']")
        if phone_number != "":
            phone_input.clear()
            phone_input.send_keys(phone_number)
            print(phone_input.get_attribute("value"))

        print("Click on 'Save Changes' button")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[class='ui blue fluid button']")
        submit_button.click()
        time.sleep(2)
        return
