from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LakesideAddCustomerSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def execute_seeds(self, email, password, first_name, last_name, birth, street_address, postal_code, city,
                      phone):
        driverIns = self.driver

        # starting
        # click add button
        print("Click on 'Search' button")
        new_customer_button = driverIns.find_element(By.CSS_SELECTOR, 'a[href="/customers/new"]')
        new_customer_button.click()

        self.edit_new_customer(email, password, first_name, last_name, birth, street_address, postal_code, city,
                               phone)

    def edit_new_customer(self, email, password, first_name, last_name, birth, street_address, postal_code, city,
                          phone):
        driverIns = self.driver

        # here, users are staying in the new customers' page
        # complementing the form
        form = driverIns.find_element(By.CSS_SELECTOR, 'form[class="ui form"]')

        # email_address
        email_input = form.find_element(By.CSS_SELECTOR, 'input[name="email"]')
        if email != "":
            email_input.clear()
            email_input.send_keys(email)
            print(email_input.get_attribute("value"))

        # password
        password_input = form.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        if password != "":
            password_input.clear()
            password_input.send_keys(password)
            print(password_input.get_attribute("value"))

        # first_name
        first_name_input = form.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
        if first_name_input != "":
            first_name_input.clear()
            first_name_input.send_keys(first_name)
            print(first_name_input.get_attribute("value"))

        # last_name
        last_name_input = form.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
        if last_name_input != "":
            last_name_input.clear()
            last_name_input.send_keys(last_name)
            print(last_name_input.get_attribute("value"))

        # birthday
        birthday_input = form.find_element(By.CSS_SELECTOR, 'input[name="birthday"]')
        if birth != "":
            birthday_input.clear()
            dates = birth.split("-")
            birthday_input.send_keys(dates[0])
            birthday_input.send_keys(Keys.RIGHT)
            birthday_input.send_keys(dates[1])
            birthday_input.send_keys(dates[2])
            print(birthday_input.get_attribute("value"))

        # street_address
        street_address_input = form.find_element(By.CSS_SELECTOR, 'input[name="streetAddress"]')
        if street_address != "":
            street_address_input.clear()
            street_address_input.send_keys(street_address)
            print(street_address_input.get_attribute("value"))

        # postal_code
        postal_code_input = form.find_element(By.CSS_SELECTOR, 'input[name="postalCode"]')
        if postal_code != "":
            postal_code_input.clear()
            postal_code_input.send_keys(postal_code)
            print(postal_code_input.get_attribute("value"))

        # city_code
        city_input = form.find_element(By.CSS_SELECTOR, 'input[name="city"]')
        if city != "":
            city_input.clear()
            city_input.send_keys(city)
            print(city_input.get_attribute("value"))

        # phone_number
        phone_input = form.find_element(By.CSS_SELECTOR, 'input[name="phoneNumber"]')
        if phone != "":
            phone_input.clear()
            phone_input.send_keys(phone)
            print(phone_input.get_attribute("value"))

        # click crete customer button
        button = form.find_element(By.CSS_SELECTOR, 'button[class="ui blue fluid button"]')
        button.click()
