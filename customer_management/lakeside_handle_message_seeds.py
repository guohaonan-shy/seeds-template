import random
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LakesideRespondNotification:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def execute_seeds(self):
        has_notification = False
        try:
            notification_part = self.driver.find_element(By.XPATH,
                                                         '//div[@class="ui segment"]//p').text
            print(notification_part)
        except NoSuchElementException:
            print("has notification")
            has_notification = True

        if not has_notification:
            return

        messages = self.driver.find_elements(By.XPATH, '//table[@class="ui blue selectable table"]//tbody//tr')

        for message in messages:
            # is_response
            is_response = bool(random.randint(0, 1))
            response_message = ""
            if is_response:
                response_message = "test hello!"
            message.click()
            time.sleep(3)
            self.response(is_response, response_message)
            # back to customer homepage
            self.driver.find_element(By.CSS_SELECTOR, 'a[href="/"]').click()



    def response(self, is_response: bool, response: str):
        # here, users stay in the profile page
        driverIns = self.driver
        chatroom = driverIns.find_element(By.CSS_SELECTOR, 'div[class="chatroom"]')

        if not is_response:
            print("don't respond message at once")
            return

        message_input = chatroom.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter a Message"]')
        message_input.clear()
        message_input.send_keys(response)
        print("response content:{}".format(message_input.get_attribute("value")))

        # send
        send_button = chatroom.find_element(By.CSS_SELECTOR, 'button[class="ui green button"]')
        send_button.click()
        print("send success")
