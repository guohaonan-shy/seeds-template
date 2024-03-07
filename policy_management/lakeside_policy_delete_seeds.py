import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LakesideDeletePolicySeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def execute_seed(self, username):
        # find the user's policies select one to edit
        # in our seed, we will handle the first one
        table = self.driver.find_element(By.CSS_SELECTOR, 'table[class="ui celled padded table"]')
        items = table.find_elements(By.XPATH, '//tbody//tr')

        for item in items:
            columns = item.find_elements(By.CSS_SELECTOR, 'td')
            if columns[1].text == username:
                columns[4].find_element(By.CSS_SELECTOR, 'a[role="button"]').click()
                time.sleep(1)
                self.policy_delete()
                break

    def policy_delete(self, policy_id = None):
        rows = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="row"]')
        # delete
        rows[0].find_element(By.CSS_SELECTOR, 'button[class="ui compact button"]').click()
        time.sleep(1)
        print("start delete......")
        # this page might produce two windows, the first one is for delete
        text_component = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[1]/div/div[2]/p')
        print(text_component.text)

        delete_button = self.driver.find_element(By.XPATH, '//div[@class="actions"]//button[@class="ui red button"]')
        delete_button.click()
        time.sleep(1)
        print("delete success......")
