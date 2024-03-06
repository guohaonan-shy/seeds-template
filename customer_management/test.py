import random
import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

import utils
from customer_management.lakeside_customer_add_customer_seeds import LakesideAddCustomerSeeds
from customer_management.lakeside_edit_customer_profile_seeds import LakesideEditCustomerProfileSeeds
from customer_management.lakeside_fetch_customer_seeds import LakeSideFetchProfileSeeds
from customer_management.lakeside_handle_message_seeds import LakesideRespondNotification
from customer_management.lakeside_search_customers_seeds import LakesideSearchSeeds


def init_customer_management_service_driver() -> webdriver:
    options = webdriver.ChromeOptions()
    options.add_argument('__no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--hide-scrollbars')

    driver = webdriver.Chrome(options=options)

    driver.set_window_size(1920, 967)

    driver.get("http://localhost:3020")
    time.sleep(1)
    return driver


class UpdateDto:
    def __init__(self, first_name: str, last_name: str, date_of_birth: str, street_address: str, postal_code: str,
                 city: str, email_address: str, phone_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = date_of_birth
        self.address = street_address
        self.postal_code = postal_code
        self.city = city
        self.email_address = email_address
        self.phone_number = phone_number
        return


class AddCustomerDto:
    def __init__(self, email, password, first_name, last_name, birth, street_address, postal_code, city,
                 phone):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.birth = birth
        self.street_address = street_address
        self.postal_code = postal_code
        self.city = city
        self.phone = phone


class MyTestCase(unittest.TestCase):
    def test_search_true(self):

        driver = init_customer_management_service_driver()

        seed = LakesideSearchSeeds(driver)
        findRes = seed.execute_seeds("a", "Fernande Levicount")

        self.assertEqual(findRes, True)
        driver.quit()

    def test_search_false(self):
        driver = init_customer_management_service_driver()

        seed = LakesideSearchSeeds(driver)
        findRes = seed.execute_seeds("a", "ghn")

        self.assertEqual(findRes, False)
        driver.quit()

    def test_fetch_profile(self):
        driver = init_customer_management_service_driver()

        seed = LakesideSearchSeeds(driver)
        target = "Fernande Levicount"
        findRes = seed.execute_seeds("a", target)

        self.assertEqual(findRes, True)

        fetchSeed = LakeSideFetchProfileSeeds(driver)
        profile = fetchSeed.execute_seeds(target)

        for key, value in profile.items():
            if key == "Name":
                self.assertEqual(value, "Fernande Levicount")
            elif key == "Address":
                self.assertEqual(value, "45267 Express Alley, 9000 St. Gallen")
            elif key == "Date of Birth":
                self.assertEqual(value, "September 12th 1957")
            elif key == "Email Address":
                self.assertEqual(value, "flevicountw@example.com")
            elif key == "Phone Number":
                self.assertEqual(value, "055 222 4111")

    def test_edit_profile(self):
        driver = init_customer_management_service_driver()

        seed = LakesideSearchSeeds(driver)
        target = "Max Mustermann"
        findRes = seed.execute_seeds("Max", target)

        self.assertEqual(findRes, True)

        fetchSeed = LakeSideFetchProfileSeeds(driver)
        profile = fetchSeed.execute_seeds(target)

        # name
        name = profile["Name"].split(" ")
        # birthday
        date_of_birthday = profile["Date of Birth"].split(sep=" ")
        year = date_of_birthday[2]
        month = utils.convertMonth(date_of_birthday[0])
        day = utils.convertDay(date_of_birthday[1])
        birthday = year + '-' + month + '-' + day
        # address
        address = profile["Address"].split(",")
        street = address[0]

        postal_city = address[1].lstrip().split(" ")
        postal, city = postal_city[0], postal_city[1]

        oldDto = UpdateDto(first_name=name[0], last_name=name[1], date_of_birth=birthday, street_address=street,
                           postal_code=postal, city=city, phone_number=profile["Phone Number"],
                           email_address=profile["Email Address"])

        newDto = UpdateDto(first_name="Maxx", last_name="Mastermann", date_of_birth="1998-04-21",
                           street_address="Redhill 100",
                           postal_code="123456", city="Singapore", email_address="xxxxxx@example.com",
                           phone_number="+864444 8783")

        s = LakesideEditCustomerProfileSeeds(driver)
        s.execute_seeds(newDto.first_name, newDto.last_name, newDto.birthday, newDto.address, newDto.postal_code,
                        newDto.city, newDto.email_address, newDto.phone_number)

        # fetch again
        print("start access profile page")
        block = driver.find_element(By.XPATH, "//div[@class='row']")
        profileRows = block.find_elements(By.CLASS_NAME, "column")
        new_profile = {}

        for row in profileRows:
            items = row.find_elements(By.CSS_SELECTOR, ".item")
            for item in items:
                try:
                    content = item.find_element(By.XPATH, ".//div[@class='content']")

                    key = content.find_element(By.XPATH, ".//div[@class='header']").text
                    value = content.find_element(By.XPATH, ".//div[@class='description']").text
                    new_profile[key] = value
                except NoSuchElementException:  # 左边列确实有一个内容为空
                    pass

        # name
        new_name = new_profile["Name"].split(" ")
        self.assertEqual(new_name[0], newDto.first_name)
        self.assertEqual(new_name[1], newDto.last_name)
        # birthday
        new_date_of_birthday = new_profile["Date of Birth"].split(sep=" ")
        new_year = new_date_of_birthday[2]
        new_month = utils.convertMonth(new_date_of_birthday[0])
        new_day = utils.convertDay(new_date_of_birthday[1])
        new_birthday = new_year + '-' + new_month + '-' + new_day
        self.assertEqual(new_birthday, newDto.birthday)
        # address
        new_address = new_profile["Address"].split(",")
        new_street = new_address[0]
        self.assertEqual(new_street, newDto.address)

        new_postal_city = new_address[1].lstrip().split(" ")
        new_postal, new_city = new_postal_city[0], new_postal_city[1]
        self.assertEqual(new_postal, newDto.postal_code)
        self.assertEqual(new_city, newDto.city)
        self.assertEqual(new_profile["Email Address"], newDto.email_address)
        self.assertEqual(new_profile["Phone Number"], newDto.phone_number[3:])

        # recover
        print("start recover......")
        s.execute_seeds(first_name=oldDto.first_name, last_name=oldDto.last_name, date_of_birth=oldDto.birthday,
                        street_address=oldDto.address,
                        postal_code=oldDto.postal_code, city=oldDto.city, email_address=oldDto.email_address,
                        phone_number=oldDto.phone_number)
        # fetch again
        print("start access profile page")
        block = driver.find_element(By.XPATH, "//div[@class='row']")
        profileRows = block.find_elements(By.CLASS_NAME, "column")
        new_profile = {}

        for row in profileRows:
            items = row.find_elements(By.CSS_SELECTOR, ".item")
            for item in items:
                try:
                    content = item.find_element(By.XPATH, ".//div[@class='content']")

                    key = content.find_element(By.XPATH, ".//div[@class='header']").text
                    value = content.find_element(By.XPATH, ".//div[@class='description']").text
                    new_profile[key] = value
                except NoSuchElementException:  # 左边列确实有一个内容为空
                    pass

        # name
        new_name = new_profile["Name"].split(" ")
        self.assertEqual(new_name[0], oldDto.first_name)
        self.assertEqual(new_name[1], oldDto.last_name)
        # birthday
        new_date_of_birthday = new_profile["Date of Birth"].split(sep=" ")
        new_year = new_date_of_birthday[2]
        new_month = utils.convertMonth(new_date_of_birthday[0])
        new_day = utils.convertDay(new_date_of_birthday[1])
        new_birthday = new_year + '-' + new_month + '-' + new_day
        self.assertEqual(new_birthday, oldDto.birthday)
        # address
        new_address = new_profile["Address"].split(",")
        new_street = address[0]
        self.assertEqual(new_street, oldDto.address)

        new_postal_city = new_address[1].lstrip().split(" ")
        new_postal, new_city = new_postal_city[0], new_postal_city[1]
        self.assertEqual(new_postal, oldDto.postal_code)
        self.assertEqual(new_city, oldDto.city)
        self.assertEqual(new_profile["Email Address"], oldDto.email_address)
        self.assertEqual(new_profile["Phone Number"], oldDto.phone_number)
        print("recover success......")
        driver.quit()

    def test_converDay(self):
        utils.convertDay("1st")

    def test_add_customer(self):
        # 1. add a new customer
        driver = init_customer_management_service_driver()

        add_customer_seed = LakesideAddCustomerSeeds(driver)

        # keep a struct to store info which is used to compare with db
        case_random_number = random.randint(a=1000000, b=9999999)

        testDto = AddCustomerDto(email="guohaonan{}@example.com".format(case_random_number),
                                 password=case_random_number, first_name="Haonan{}".format(case_random_number),
                                 last_name="Guo", birth="1998-04-21",
                                 street_address="redhill {}".format(case_random_number),
                                 postal_code=random.randint(1000, 9999), city="Singapore",
                                 phone="+86 {} {}".format(random.randint(0000, 9999), random.randint(0000, 9999)))

        add_customer_seed.execute_seeds(email=testDto.email, password=testDto.password, first_name=testDto.first_name,
                                        last_name=testDto.last_name, birth=testDto.birth,
                                        street_address=testDto.street_address, postal_code=testDto.postal_code,
                                        city=testDto.city, phone=testDto.phone)

        # compare and assert that the customer info is the same with expectation
        search_seeds = LakesideSearchSeeds(driver)
        target = "{} {}".format(testDto.first_name, testDto.last_name)
        search_seeds.search(testDto.first_name, target)

        # handle search result
        fetchSeed = LakeSideFetchProfileSeeds(driver)
        profile = fetchSeed.execute_seeds(target)

        for key, value in profile.items():
            if key == "Name":
                self.assertEqual(value, target)
            elif key == "Address":
                self.assertEqual(value, "{}, {} {}".format(testDto.street_address, testDto.postal_code, testDto.city))
            elif key == "Date of Birth":
                self.assertEqual(value, "April 21st 1998")
            elif key == "Email Address":
                self.assertEqual(value, testDto.email)
            elif key == "Phone Number":
                self.assertEqual("+86 {}".format(value), testDto.phone)

        driver.quit()

    def test_response(self):
        driver = init_customer_management_service_driver()

        # todo: 先这样，后续完成注册seeds，可以构建自动化case
        # 这里先手动用test账号构建一些消息
        response_seeds = LakesideRespondNotification(driver)
        response_seeds.execute_seeds()

        driver.quit()


if __name__ == '__main__':
    unittest.main()
