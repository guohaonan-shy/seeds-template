import time

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def init_nicefish_driver() -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument('__no-sandbox')
    # options.add_argument('--headless')
    options.add_argument('--hide-scrollbars')

    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

    driver = webdriver.Chrome(options=options)

    driver.set_window_size(1920, 1080)

    driver.get("http://172.26.190.201:8091/post")
    # main page starts from http://172.26.190.201:8091 to http://172.26.190.201:8091/post
    time.sleep(2)
    return driver