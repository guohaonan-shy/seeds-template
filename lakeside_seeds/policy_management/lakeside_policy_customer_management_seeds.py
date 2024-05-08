import time

from typing import Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from lakeside_seeds.policy_management.lakeside_agreement import Agreement
from lakeside_seeds.policy_management.lakeside_policy_edit_seeds import LakesideEditPolicySeeds


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

    def jump_to_customer_management(self):
        open_customer_management_button = self.driver.find_element(By.CSS_SELECTOR,
                                                                   'button[class="ui compact right floated mini button"]')
        open_customer_management_button.click()
        time.sleep(1)
        print("jump to the management......")

    def click_risk_factor(self):
        risk_button = self.driver.find_element(By.CSS_SELECTOR, 'button[class="ui circular compact icon tiny button"]')
        risk_button.click()
        time.sleep(1)
        print("click to look at risk factor explanation......")

        window = self.driver.find_element(By.CSS_SELECTOR, 'div[class="ui standard modal transition visible active"]')
        explanation = window.find_element(By.XPATH, './/div[@class="content"]//div[@class ="description"]//p').text
        print(explanation)

        ok_button = self.driver.find_element(By.CSS_SELECTOR,
                                             'button[class="modalButton ui right floated positive button"]')
        ok_button.click()
        print("back to the customer page......")

    def get_risk_factor(self) -> int:
        value_str = self.driver.find_element(By.CSS_SELECTOR, 'div[class="value"]').text
        print("risk factor: ", value_str)
        return int(value_str)

    def create_new_policy(self, start_date: str, end_date: str, policy_type: str, deduct: int, insurance_premium: int,
                          policy_limit: int,
                          agreements: list[Agreement]):
        # uid = self.driver.current_url.split('/')[-1]
        # uri = "/customers/" + uid + "/policies/new"
        new_policy_button = self.driver.find_element(By.CSS_SELECTOR,
                                                     'a[class="ui green compact right floated tiny button"]')
        new_policy_button.click()
        time.sleep(1)

        print("start adding a new policies......")
        LakesideEditPolicySeeds(self.driver).policy_edit(start_date, end_date, policy_type, deduct, insurance_premium,
                                                         policy_limit, agreements, True)
        print("done......")
