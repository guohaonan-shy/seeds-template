import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class NicefishCommentSeeds:
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
                target_post = self.driver.find_element(By.CSS_SELECTOR,
                                                           'a[href="/post/post-detail/{}"]'.format(target_post_id))
            except NoSuchElementException:
                print("no target post on homepage......")
                return

        # jump the detail page
        time.sleep(2)
        target_post.click()
        time.sleep(2)
        print("direct to the detail page")

    def execute_seeds(self, comment=""):
        # comment
        print("start commenting the post......")
        comment_form = self.driver.find_element(By.XPATH, '/html/body/div/div[4]/div/div/div/div[2]/form')
        # input the comment
        content_input = comment_form.find_element(By.CSS_SELECTOR, 'textarea[name="content"]')
        content_input.clear()
        content_input.send_keys(comment)
        # input the captcha
        captcha_input = comment_form.find_element(By.CSS_SELECTOR, 'input[name="captcha"]')
        captcha_input.send_keys("0")
        time.sleep(2)
        # submit
        submit_button = comment_form.find_element(By.CSS_SELECTOR, 'button[class="btn btn-success"]')
        submit_button.click()
        time.sleep(2)
        print("edit post success......")
