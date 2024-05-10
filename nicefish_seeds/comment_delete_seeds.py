import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class NicefishCommentDeleteSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def jump_to_comment_management_page(self):
        setting_button = self.driver.find_element(By.CSS_SELECTOR, 'a[class="nav-link"][href="/manage/chart"]')
        setting_button.click()
        time.sleep(2)
        print("direct to setting page......")

        post_table_button = self.driver.find_element(By.CSS_SELECTOR,
                                                     'a[class="list-group-item"][href="/manage/comment-table"]')
        post_table_button.click()
        time.sleep(2)
        print("direct to comment management......")

    def execute_seeds(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR,
                                            'button[class="p-button p-component p-button-danger p-button-icon-only"]')
        # the first one
        delete_button = rows[-1]
        time.sleep(2)

        delete_button.click()
        time.sleep(2)

        # confirm
        window = self.driver.find_element(By.CSS_SELECTOR, 'div[class="p-dialog-footer"]')
        window.find_element(By.CSS_SELECTOR, 'button[aria-label="Yes"]').click()
        time.sleep(1)

        print("delete success......")