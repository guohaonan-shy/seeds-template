import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class NicefishCollectSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # at present, we just access the fixed post
    def jump_to_detail(self, target_post_id=0):
        print("start browsing......")
        if target_post_id == 0:
            columns = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="my-masonry-grid_column"]')
            # in this case, we just simulate the behavior of comment, so we choose the element which is located at the first row and the first column
            posts = columns[0].find_elements(By.CSS_SELECTOR, 'section[class="post-list-item"]')
            target_post = posts[0].find_element(By.CSS_SELECTOR, 'a[href^="/post/post-detail/"]')
        else:
            try:
                target_post = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/post/post-detail/{}"]'.format(target_post_id))
            except NoSuchElementException:
                print("no target post on homepage......")
                return

        # jump the detail page
        time.sleep(2)
        target_post.click()
        time.sleep(2)
        print("direct to the detail page")

    def execute_seeds(self):
        print("start handling collect or cancel collection behavior......")
        right_bar = self.driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div/div/div[1]/div[1]/div[2]')

        collect_button = right_bar.find_element(By.CSS_SELECTOR, 'span[class="fa fa-star op-icon-basic"]')
        style_attr = collect_button.get_attribute("style")

        if style_attr == "":
            print("ready to collect......")
        else:
            print("ready to cancel collection......")

        collect_button.click()
        time.sleep(1)
        print("collect or cancel collection success......")