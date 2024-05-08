import time

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def convertMonth(month: str):
    if month == "January":
        return "01"
    elif month == "February":
        return "02"
    elif month == "March":
        return "03"
    elif month == "April":
        return "04"
    elif month == "May":
        return "05"
    elif month == "June":
        return "06"
    elif month == "July":
        return "07"
    elif month == "August":
        return "08"
    elif month == "September":
        return "09"
    elif month == "October":
        return "10"
    elif month == "November":
        return "11"
    else:
        return "12"


def convertMonthV2(month: str):
    if month == "Jan":
        return "01"
    elif month == "Feb":
        return "02"
    elif month == "Mar":
        return "03"
    elif month == "Apr":
        return "04"
    elif month == "May":
        return "05"
    elif month == "Jun":
        return "06"
    elif month == "Jul":
        return "07"
    elif month == "Aug":
        return "08"
    elif month == "Sept":
        return "09"
    elif month == "Oct":
        return "10"
    elif month == "Nov":
        return "11"
    else:
        return "12"


def convertDay(day: str):
    value = 0
    for byte in day:
        if 0 <= ord(byte) - ord('0') <= 9:
            value = value * 10 + ord(byte) - ord('0')
    if value < 10:
        return "0" + str(value)
    return str(value)

def init_customer_management_service_driver() -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument('__no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--hide-scrollbars')

    driver = webdriver.Chrome(options=options)

    driver.set_window_size(1920, 967)

    driver.get("http://localhost:3020")
    time.sleep(1)
    return driver

def init_customer_self_service_driver() -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument('__no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--hide-scrollbars')

    driver = webdriver.Chrome(options=options)

    driver.set_window_size(1920, 967)

    driver.get("http://localhost:3000")
    time.sleep(1)
    return driver


def init_policy_service_driver() -> WebDriver:
    options = webdriver.ChromeOptions()
    options.add_argument('__no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--hide-scrollbars')

    driver = webdriver.Chrome(options=options)

    driver.set_window_size(1920, 967)

    driver.get("http://localhost:3010")
    time.sleep(1)
    return driver