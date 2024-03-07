import time

from typing import Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LakesidePolicyCustomerManagementSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def jump_to_customer(self):
        # from http://localhost:3010/* jump to the customer
        print("jump to the customer tab......")
        customers_tab = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/customers"]')
        customers_tab.click()
        time.sleep(1)

    def search(self, condition, target_username) -> Optional[str]:
        # type search condition and find target username
        print("start searching......")
        search_input = self.driver.find_element(By.CSS_SELECTOR, 'input[data-v-558141d5=""]')
        search_input.click()
        time.sleep(1)
        search_input.send_keys(condition)

        search_button = self.driver.find_element(By.CSS_SELECTOR, 'button[class="ui primary button"]')
        search_button.click()
        time.sleep(1)
        print("finish searching......")

        # handle search results
        print("start handing table......")
        items = self.driver.find_elements(By.XPATH, '/html/body/div/div[2]/div/table/tbody/tr')
        # items might include the profile history, it means one user can have more than one data records
        # need to filter duplicates
        unique = set()
        for item in items:
            columns = item.find_elements(By.CSS_SELECTOR, 'td')
            customer_policy_button = columns[3].find_element(By.CSS_SELECTOR, 'a')
            uid = customer_policy_button.get_attribute("href").split("/")[-1]
            if uid in unique:
                continue
            else:
                if columns[0].text == target_username:
                    customer_policy_button.click()
                    time.sleep(1)
                    return uid
        return None
