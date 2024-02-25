import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LakeSideFetchProfileSeeds:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def execute_seeds(self, target):

        # now, driver stop at the page that include target

        table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                # (By.CSS_SELECTOR, 'table[class="ui celled table"]')
                (By.XPATH, "//table[@class='ui celled table']//tbody//tr")
            )
        )

        rows = table.find_elements(By.XPATH, "//td[1]")

        for row in rows:
            if row.text == target:
                element = table.find_element(By.XPATH, "//td[4]")
                link = element.find_element(By.XPATH, "//a[@class='ui button']")
                print("click link to the profile page")
                link.click()
                break

        time.sleep(2)

        print("start access profile page")
        block = self.driver.find_element(By.XPATH, "//div[@class='row']")
        profileRows = block.find_elements(By.CLASS_NAME, "column")
        profile = {}

        for row in profileRows:
            items = row.find_elements(By.CSS_SELECTOR, ".item")
            for item in items:
                try:
                    content = item.find_element(By.XPATH, ".//div[@class='content']")

                    key = content.find_element(By.XPATH, ".//div[@class='header']").text
                    value = content.find_element(By.XPATH, ".//div[@class='description']").text
                    profile[key] = value
                except NoSuchElementException:  # 左边列确实有一个内容为空
                    pass
        return profile

