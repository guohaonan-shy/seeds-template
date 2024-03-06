import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utils import convertMonthV2


class LakesideFetchPolicySeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # def execute_seeds(self, username):
    #     # find the user's policies select one to edit
    #     # in our seed, we will handle the first one
    #     table = self.driver.find_element(By.CSS_SELECTOR, 'table[class="ui celled padded table"]')
    #     items = table.find_elements(By.XPATH, '//tbody//tr')
    #
    #     for item in items:
    #         columns = item.find_elements(By.CSS_SELECTOR, 'td')
    #         if columns[1].text == username:
    #             columns[4].find_element(By.CSS_SELECTOR, 'a[role="button"]').click()
    #             time.sleep(1)
    #             res = self.find_policy()
    #             return res
    #
    #     return {}

    def find_policy(self):
        rows = self.driver.find_elements(By.XPATH, '//div[@class="ui two column grid"]/div[@class="row"]')
        # policy_type
        policy_type = rows[0].find_element(By.XPATH, '//div[@class="eight wide column"]//h3').text

        # period
        spans = rows[3].find_elements(By.CSS_SELECTOR, 'span')

        # start_date
        start_date = spans[0].text
        middle1 = start_date.split('. ')
        day = middle1[0]
        middle2 = middle1[1].split(' ')
        month = convertMonthV2(middle2[0])
        year = middle2[1]
        start_date_format = year + '-' + month + '-' + day

        # end_date
        end_date = spans[1].text
        middle1 = end_date.split('. ')
        day = middle1[0]
        middle2 = middle1[1].split(' ')
        month = convertMonthV2(middle2[0])
        year = middle2[1]
        end_date_format = year + '-' + month + '-' + day

        # deduct
        deduct = rows[4].find_element(By.CSS_SELECTOR, 'div[class="middle aligned twelve wide column"]').text
        # premium
        premium = rows[5].find_element(By.CSS_SELECTOR, 'div[class="middle aligned twelve wide column"]').text
        # policy_limit
        policy_limit = rows[6].find_element(By.CSS_SELECTOR, 'div[class="middle aligned twelve wide column"]').text

        res = {"start_date": start_date_format, "end_date": end_date_format, "deduct": deduct, "insurance_premium": premium,
               "policy_limit": policy_limit, "policy_type":policy_type}
        return res
