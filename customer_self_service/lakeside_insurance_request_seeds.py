import random
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LakesideRequestInsuranceSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def execute_seeds(self):
        # stay in /host:3000/policies
        print("start request new insurance quote......")
        request_button = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/policies/new-insurance-quote-request"]')
        request_button.click()
        time.sleep(1)

        # 1. personal data
        print("start handling personal data......")
        # 1.1 contact address
        # don't modify
        # 1.2 Bill address
        # the same as contact address
        try:
            print("same option is checked......")
            _ = self.driver.find_element(By.CSS_SELECTOR, 'div[class="ui checked checkbox"]')
        except NoSuchElementException:
            print("same option is not checked......")
            same_option = self.driver.find_element(By.CSS_SELECTOR, 'div[class="ui checkbox"]')
            same_option.click()

        print("finish handling personal data......")
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button[class="ui icon right floated right labeled button"]').click()
        time.sleep(1)
        # insurance
        print("start handling insurance......")
        options = self.driver.find_elements(By.XPATH, '//form[@class="ui form"]//div[@class="field"]')
        # start_date default start from the current day: options[0]
        # insurance_type
        insurance_dropbox = options[1].find_element(By.CSS_SELECTOR, 'div[role="listbox"]')
        insurance_dropbox.click()
        insurance_types = insurance_dropbox.find_elements(By.CSS_SELECTOR, 'div[role="option"]')
        choice = random.randint(0, len(insurance_types)-1)
        insurance_types[choice].click()
        # deductible
        deduct_dropbox = options[2].find_element(By.CSS_SELECTOR, 'div[role="listbox"]')
        deduct_dropbox.click()
        deduct_types = deduct_dropbox.find_elements(By.CSS_SELECTOR, 'div[role="option"]')
        choice = random.randint(0, len(deduct_types) - 1)
        deduct_types[choice].click()

        print("finish handling insurance......")
        self.driver.find_element(By.CSS_SELECTOR,
                                 'button[class="ui icon right floated right labeled button"]').click()
        time.sleep(1)
        # confirm

        self.driver.find_element(By.CSS_SELECTOR,
                                 'button[class="ui primary right floated button"]').click()
        time.sleep(1)

    def jump_to_policies(self):
        if self.driver.current_url == "http://localhost:3000/policies":
            return

        if self.driver.current_url == "http://localhost:3000/profile" or "http://localhost:3000/contact":
            policies_tab = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/policies"]')
            policies_tab.click()
            time.sleep(1)
            return

        print("call panic")