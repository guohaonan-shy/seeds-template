import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class NicefishFollowSeeds:
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

    def get_current_follows(self) -> int:
        print("start accessing the user homepage......")
        self.driver.find_element(By.CSS_SELECTOR, 'a[class="nav-link"][href^="/user-home/"]').click()
        time.sleep(1)
        print("direct to the user homepage......")

        following_cnt = self.driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div[1]/div[2]/div[1]/p[2]/span[2]')
        cnt = int(following_cnt.text)
        self.driver.find_element(By.CSS_SELECTOR, 'a[href="/post"]').click()
        time.sleep(1)
        print("back to homepage......")
        return cnt

    def execute_seeds(self):
        print("start following or unfollowing the post......")
        right_bar = self.driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div/div/div[1]/div[1]/div[2]')

        follow_button = right_bar.find_element(By.CSS_SELECTOR, 'span[class*="op-follow"]')
        class_attr = follow_button.get_attribute("class")

        str_list = class_attr.split(" ")
        if str_list[1] == "fa-plus-circle":
            print("ready to follow......")
        else:
            print("ready to unfollow......")

        follow_button.click()
        time.sleep(1)
        print("follow or unfollow success......")
