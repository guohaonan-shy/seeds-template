from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LakesideSearchSeeds:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        pass

    def execute_seeds(self, condition: str, target: str):
        # 这块也是个拓展点，构建符合条件的搜索条件
        self.search(condition, target)
        return self.search_handle(target)

    def search(self, condition: str, target: str):
        driverIns = self.driver

        # starting
        # input search key
        print("Input customer name that we want to find......")
        search_input = driverIns.find_element(By.CSS_SELECTOR, 'input[placeholder="Search..."]')
        search_input.clear()
        search_input.send_keys(condition)

        print("Click on 'Search' button")
        submit_button = driverIns.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()

        return

    def search_handle(self, target):
        print("Search result Handle")
        # search result is more than 10?

        table = self.driver.find_element(By.XPATH, "//table[@class='ui celled table']")
        foot = table.find_element(By.XPATH, ".//tfoot//tr")
        tags = foot.find_elements(By.TAG_NAME, "th")

        cntBlock = tags[0]
        listBlock = tags[1]

        total = int(cntBlock.text.split(sep=" of ")[1])
        print(total)

        iterCnt = total // 10 if total % 10 == 0 else total // 10 + 1

        res = False

        for i in range(iterCnt):

            itable = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//table[@class='ui celled table']//tbody//tr")
                )
            )

            rows = itable.find_elements(By.XPATH, "//td[1]")

            for row in rows:
                if row.text == target:
                    res = True
                    break

            if res:
                print("Find Target !!!!")
                break

            next = listBlock.find_element(By.XPATH, ".//div[@class='ui pagination right floated menu']/a[2]")
            print(next.get_attribute("class"))
            if next.get_attribute("class") == "icon item":
                next.click()

        return res
