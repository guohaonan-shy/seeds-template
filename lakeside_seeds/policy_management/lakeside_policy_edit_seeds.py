import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Keys

from lakeside_seeds.policy_management.lakeside_agreement import Agreement


class LakesideEditPolicySeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def execute_seed(self, username, start_date: str, end_date: str, policy_type: str, deduct: int,
                     insurance_premium: int, policy_limit: int,
                     agreements=None):
        # find the user's policies select one to edit
        # in our seed, we will handle the first one
        if agreements is None:
            agreements = []
        table = self.driver.find_element(By.CSS_SELECTOR, 'table[class="ui celled padded table"]')
        items = table.find_elements(By.XPATH, '//tbody//tr')

        for item in items:
            columns = item.find_elements(By.CSS_SELECTOR, 'td')
            if columns[1].text == username:
                columns[4].find_element(By.CSS_SELECTOR, 'a[role="button"]').click()
                time.sleep(1)
                self.policy_edit(start_date, end_date, policy_type, deduct, insurance_premium, policy_limit, agreements)
                break

    def policy_edit(self, start_date: str, end_date: str, policy_type: str, deduct: int, insurance_premium: int,
                    policy_limit: int,
                    agreements: list[Agreement], from_policy_page=False):
        if not from_policy_page:
            rows = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="row"]')
            # edit
            rows[0].find_element(By.CSS_SELECTOR, 'a[class="ui compact button"]').click()
            time.sleep(1)
        print("start editing......")
        rows = self.driver.find_elements(By.XPATH,
                                         '//form[@class="ui form"]//div[@class="ui two column internally celled grid"]/div[@class="row"]')

        # period
        dates = rows[0].find_elements(By.CSS_SELECTOR, 'input[type="date"]')
        # start_date
        start_date_str = start_date.split('-')
        dates[0].clear()
        dates[0].send_keys(start_date_str[0])
        dates[0].send_keys(Keys.RIGHT)
        dates[0].send_keys(start_date_str[1])
        dates[0].send_keys(start_date_str[2])
        # end_date
        end_date_str = end_date.split('-')
        dates[1].clear()
        dates[1].send_keys(end_date_str[0])
        dates[1].send_keys(Keys.RIGHT)
        dates[1].send_keys(end_date_str[1])
        dates[1].send_keys(end_date_str[2])

        # policy_type
        dropbox = rows[1].find_element(By.CSS_SELECTOR, 'div[role="listbox"]')
        dropbox.click()
        time.sleep(1)
        options = dropbox.find_elements(By.CSS_SELECTOR, 'div[role="option"]')
        for option in options:
            if option.text == policy_type:
                option.click()
                time.sleep(1)
                break

        # deduct
        deduct_input = rows[2].find_element(By.CSS_SELECTOR, 'input[placeholder="Amount in CHF"]')
        deduct_input.clear()
        deduct_input.send_keys(str(deduct))
        # premium
        premium_input = rows[3].find_element(By.CSS_SELECTOR, 'input[placeholder="Amount in CHF"]')
        premium_input.clear()
        premium_input.send_keys(str(insurance_premium))
        # policy_limit
        policy_limit_input = rows[4].find_element(By.CSS_SELECTOR, 'input[placeholder="Amount in CHF"]')
        policy_limit_input.clear()
        policy_limit_input.send_keys(str(policy_limit))
        # agreement
        if len(agreements) > 0:
            add_button = rows[5].find_element(By.CSS_SELECTOR, 'button[class="ui green tiny button"]')
            for _ in agreements:
                add_button.click()
                time.sleep(1)
            # /div[@class="two column row"]//div[class="fourteen wide column"]
            forms = rows[5].find_elements(By.CSS_SELECTOR, 'div[class="fourteen wide column"]')
            old_forms_cnt = len(forms) - len(agreements)
            for i in range(old_forms_cnt, len(forms)):
                # title
                title_input = forms[i].find_element(By.CSS_SELECTOR, 'input[placeholder="Title"]')
                title_input.clear()
                title_input.send_keys(agreements[i-old_forms_cnt].title)
                # description
                description_input = forms[i].find_element(By.CSS_SELECTOR, 'textarea[placeholder="Description"]')
                description_input.clear()
                description_input.send_keys(agreements[i-old_forms_cnt].description)

        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        time.sleep(1)
        print("edit success......")
