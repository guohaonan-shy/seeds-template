import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class NicefishAccessWriterSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # at present, we just access the fixed post
    def jump_from_homepage(self):
        print("start browsing......")
        columns = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="my-masonry-grid_column"]')
        # in this case, we just simulate the behavior of comment, so we choose the element which is located at the first row and the first column
        posts = columns[0].find_elements(By.CSS_SELECTOR, 'section[class="post-list-item"]')
        target_post = posts[0]

        # jump the detail page
        writer_page_link = target_post.find_element(By.CSS_SELECTOR, 'a[href^="/user-home/"]')
        writer_page_link.click()
        time.sleep(1)
        print("direct to the writer profile page")

    def jump_from_post_detail_page(self):
        print("start access writer page from post detail page......")
        component = self.driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div/div/div[1]/div[2]')
        component.find_element(By.CSS_SELECTOR, 'a[href^="/user-home/"]').click()
        time.sleep(1)
        print("direct to the writer page......")

    def get_likes(self) -> int:
        like_cnt_component = self.driver.find_element(By.XPATH,
                                                      '/html/body/div/div[4]/div/div[1]/div[2]/div[1]/p[3]/span[2]')
        cnt = int(like_cnt_component.text)
        return cnt
