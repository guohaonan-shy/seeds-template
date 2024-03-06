import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LakesideRespondQuoteRequestSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def execute_seeds(self, username) -> str:
        items = self.driver.find_elements(By.XPATH, '/html/body/div/div[2]/div/table[1]/tbody/tr')

        for item in items:
            columns = item.find_elements(By.CSS_SELECTOR, 'td')
            name = columns[1].find_element(By.CSS_SELECTOR, 'a').text
            status = columns[3].find_element(By.CSS_SELECTOR, 'i').text
            if name == username and status == "Request open":
                detail_button = columns[4].find_element(By.CSS_SELECTOR, 'a[class="ui compact small button"]')
                policy_id = detail_button.get_attribute("href").split('/')[-1]
                detail_button.click()
                time.sleep(1)
                self.respond()
                return policy_id

    def jump_to_quote_request(self):
        quote_tab = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/insurance-quote-requests"]')
        quote_tab.click()
        time.sleep(1)
        return

    def respond(self, is_accept=True, expiration_date="2030-12-31 23:59", insurance_premium=10000, policy_limit=10000):
        respond_button = self.driver.find_element(By.CSS_SELECTOR, 'button[class="ui blue compact mini button"]')
        respond_button.click()
        time.sleep(1)

        respond_window = self.driver.find_element(By.CSS_SELECTOR,
                                                  'div[class="ui small modal transition visible active"]')

        content = respond_window.find_element(By.CSS_SELECTOR, 'form[class="ui form"]')

        # accept or reject
        if is_accept:
            content.find_element(By.ID, 'accept').click()
        else:
            content.find_element(By.ID, 'reject').click()
        time.sleep(1)
        confirm_button = respond_window.find_element(By.CSS_SELECTOR, 'button[class="ui disabled positive button"]')

        if not is_accept:
            confirm_button.click()
            time.sleep(1)
            return

        # expiration date
        middle = expiration_date.split(' ')
        date_list = middle[0].split('-')
        time_str = middle[1].split(':')

        expiration_date_input = content.find_element(By.CSS_SELECTOR, 'input[type="datetime-local"]')
        expiration_date_input.send_keys(date_list[0])
        expiration_date_input.send_keys(Keys.RIGHT)
        expiration_date_input.send_keys(date_list[1])
        expiration_date_input.send_keys(date_list[2])

        expiration_date_input.send_keys(time_str[0])
        expiration_date_input.send_keys(time_str[1])

        inputs = content.find_elements(By.CSS_SELECTOR, 'input[placeholder="Amount in CHF"]')
        # insurance_premium
        inputs[0].send_keys(str(insurance_premium))
        # policy_limit
        inputs[1].send_keys(str(policy_limit))

        confirm_button.click()
        time.sleep(1)
