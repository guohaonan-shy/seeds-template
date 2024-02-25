import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from customer_management.lakeside_search_customers_seeds import LakesideSearchSeeds


def profile():
    print("start access profile page")
    block = driver.find_element(By.XPATH, "//div[@class='row']")
    rows = block.find_elements(By.CLASS_NAME, "column")
    profile = {}

    for row in rows:
        items = row.find_elements(By.CSS_SELECTOR, ".item")
        for item in items:
            try:
                content = item.find_element(By.XPATH, ".//div[@class='content']")

                key = content.find_element(By.XPATH, ".//div[@class='header']").text
                value = content.find_element(By.XPATH, ".//div[@class='description']").text
                profile[key] = value
            except NoSuchElementException:  # 左边列确实有一个内容为空
                pass

    # print
    for key, value in profile.items():
        print("", key, ":", "\t", value)


class LakeSideFetchProfileSeeds():

    def __init__(self) -> None:
        self.searchSeeds = LakesideSearchSeeds()

    def execute_seeds(self, driver: WebDriver):
        s = self.searchSeeds
        # starting......
        s.search(driver, "Fernande")

        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                # (By.CSS_SELECTOR, 'table[class="ui celled table"]')
                (By.XPATH, "//table[@class='ui celled table']//tbody//tr")
            )
        )

        print("click link to the profile page")
        element = table.find_element(By.XPATH, "//td[4]")
        link = element.find_element(By.XPATH, "//a[@class='ui button']")
        link.click()
        time.sleep(3)

        profile()


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('__no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--hide-scrollbars')

    driver = webdriver.Chrome(options=options)

    driver.set_window_size(1920, 967)

    driver.get("http://localhost:3020")

    seed = LakeSideFetchProfileSeeds()
    seed.execute_seeds(driver=driver)

    driver.quit()
