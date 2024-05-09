import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class NicefishLikeSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # at present, we just access the fixed post
    def jump_to_detail(self):
        print("start browsing......")
        columns = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="my-masonry-grid_column"]')
        # in this case, we just simulate the behavior of comment, so we choose the element which is located at the first row and the first column
        posts = columns[0].find_elements(By.CSS_SELECTOR, 'section[class="post-list-item"]')
        target_post = posts[0]

        # jump the detail page
        detail_page_link = target_post.find_element(By.CSS_SELECTOR, 'a[href^="/post/post-detail/"]')
        detail_page_link.click()
        time.sleep(1)
        print("direct to the detail page")

    def execute_seeds(self):
        print("start handling like or unlike behavior......")
        right_bar = self.driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div/div/div[1]/div[1]/div[2]')

        like_button = right_bar.find_element(By.CSS_SELECTOR, 'span[class="fa fa-heart op-icon-basic"]')
        style_attr = like_button.get_attribute("style")

        if style_attr == "":
            print("ready to like......")
        else:
            print("ready to unlike......")

        like_button.click()
        time.sleep(1)
        print("like or unlike success......")
