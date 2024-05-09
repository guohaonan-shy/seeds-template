import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class NicefishPostDeleteSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def jump_to_post_management_page(self):
        setting_button = self.driver.find_element(By.CSS_SELECTOR, 'a[class="nav-link"][href="/manage/chart"]')
        setting_button.click()
        time.sleep(2)
        print("direct to setting page......")

        post_table_button = self.driver.find_element(By.CSS_SELECTOR,
                                                     'a[class="list-group-item"][href="/manage/post-table"]')
        post_table_button.click()
        time.sleep(2)
        print("direct to post management......")

    def execute_seeds(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR, 'tr[role="row"]')
        # the first one
        target = rows[0]
        delete_button = target.find_element(By.CSS_SELECTOR,
                                            'button[class="p-button p-component p-button-danger p-button-icon-only"]')

        delete_button.click()
        time.sleep(2)
        print("delete success......")
