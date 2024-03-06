import random
import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from customer_management.lakeside_search_customers_seeds import LakesideSearchSeeds
from customer_management.test import init_customer_management_service_driver
from customer_self_service.lakeside_complete_user_profile_seeds import LakesideCompleteProfileSeeds
from customer_self_service.lakeside_insurance_request_seeds import LakesideRequestInsuranceSeeds
from customer_self_service.lakeside_login_seeds import LakesideLoginSeeds
from customer_self_service.lakeside_logout_seeds import LakesideLogoutSeeds
from customer_self_service.lakeside_register_seeds import LakesideRegisterNewUserSeeds


def init_customer_self_service_driver() -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument('__no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--hide-scrollbars')

    driver = webdriver.Chrome(options=options)

    driver.set_window_size(1920, 967)

    driver.get("http://localhost:3000")
    return driver


class MyTestCase(unittest.TestCase):
    def test_register_login(self):
        driver = init_customer_self_service_driver()
        # register
        register_seed = LakesideRegisterNewUserSeeds(driver)
        test_register_email = "testUserCase{}@example.com".format(random.randint(0, 10000))
        print("email: ", test_register_email)
        test_password = random.randint(100000, 999999)
        print("password: ", test_password)
        register_seed.execute_seeds(test_register_email, test_password)
        time.sleep(1)
        # login
        login_seed = LakesideLoginSeeds(driver)
        login_seed.execute_seeds(from_signup=True, email=test_register_email, password=test_password)
        time.sleep(1)
        # complete_profile
        complete_seed = LakesideCompleteProfileSeeds(driver)
        first_name = "User{}".format(random.randint(0, 10000))
        print(first_name)
        complete_seed.execute_seeds(first_name=first_name, last_name="Test", street_address="test address",
                                    postal_code="1000", city="test city", phone="+86 9999 9999", birthday="1900-01-01")
        time.sleep(1)
        # at this time, we can fetch information from customer management info
        customer_customer_driver = init_customer_management_service_driver()

        seed = LakesideSearchSeeds(customer_customer_driver)
        findRes = seed.execute_seeds("User", "{} Test".format(first_name))

        self.assertEqual(findRes, True)

        # logout
        logout_seed = LakesideLogoutSeeds(driver)
        logout_seed.execute_seeds()
        time.sleep(1)

        customer_customer_driver.quit()
        driver.quit()

    def test_request_insurance(self):
        driver = init_customer_self_service_driver()
        # login
        login_seed = LakesideLoginSeeds(driver)
        login_seed.execute_seeds(from_signup=False, email="testUser10001@example", password="123456")

        #
        try:
            requests = driver.find_elements(By.XPATH, '//table[@class="ui selectable table"]//tbody//tr')
        except NoSuchElementException:
            print("there is not requests for this user")
            requests = []

        old_cnt = len(requests)

        request_insurance_seed = LakesideRequestInsuranceSeeds(driver)
        request_insurance_seed.execute_seeds()

        try:
            requests = driver.find_elements(By.XPATH, '//table[@class="ui selectable table"]//tbody//tr')
        except NoSuchElementException:
            print("there is not requests for this user")
            requests = []

        new_cnt = len(requests)

        self.assertEqual(new_cnt-old_cnt,  1)
        driver.quit()

if __name__ == '__main__':
    unittest.main()
