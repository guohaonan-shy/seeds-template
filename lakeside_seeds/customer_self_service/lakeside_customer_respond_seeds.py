import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LakesideCustomerRespondSeeds:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def execute_seeds(self, is_accept=True):
        print("start handling all of need to handle requests......")
        quote_requests = self.driver.find_elements(By.XPATH, '/html/body/div/div/div[2]/table/tbody/tr')

        for quote_request in quote_requests:
            columns = quote_request.find_elements(By.CSS_SELECTOR, 'td')
            status = columns[2].find_element(By.CSS_SELECTOR, "i").text
            if status == "Insurance Quote available":
                quote_request.click()
                time.sleep(1)

                policy_id = self.driver.current_url.split('/')[-1]
                if is_accept:
                    accept_button = self.driver.find_element(By.CSS_SELECTOR, 'button[class="ui green mini compact button"]')
                    accept_button.click()
                else:
                    reject_button = self.driver.find_element(By.CSS_SELECTOR,'button[class="ui red mini compact button"]')
                    reject_button.click()
                time.sleep(1)
                return policy_id
        print("finish handling all of need to handle requests......")