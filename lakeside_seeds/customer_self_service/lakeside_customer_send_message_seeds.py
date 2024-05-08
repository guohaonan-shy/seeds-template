import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LakesideCustomerSendMessageSeeds:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def execute_seed(self, message="test send"):
        chatroom = self.driver.find_element(By.CSS_SELECTOR, 'div[class="chatroom"]')

        message_input = chatroom.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter a Message"]')
        message_input.clear()
        message_input.send_keys(message)
        print("send message content:{}".format(message_input.get_attribute("value")))

        # send
        send_button = chatroom.find_element(By.CSS_SELECTOR, 'button[class="ui green button"]')
        send_button.click()
        print("send success")
        time.sleep(1)

    def jump_to_contact(self):
        if self.driver.current_url == "http://localhost:3000/contact":
            return

        if self.driver.current_url == "http://localhost:3000/profile" or "http://localhost:3000/policies":
            contact_tab = self.driver.find_element(By.CSS_SELECTOR, 'a[href="/contact"]')
            contact_tab.click()
            time.sleep(1)
            return

        print("call panic")
