import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == "__main__":

    options = webdriver.ChromeOptions()
    options.add_argument('__no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--hide-scrollbars')

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 967)

    driver.get("http://localhost:3020")
    time.sleep(3)
    print("Input customer name that we want to find......")
    search_input = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Search..."]')
    search_input.send_keys("y")

    print("Click on 'Search' button")
    submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

    print("Search result Handle")
    # 前端输出是分页后的结果，需要判断是否要到下一页
    # 对于搜索行为，到这里我觉得就可以
    # 这个函数可以抽象成获取目标值，那么就需要考虑分页的
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            # (By.CSS_SELECTOR, 'table[class="ui celled table"]')
            (By.XPATH, "//table[@class='ui celled table']//tbody//tr")
        )
    )

    rows = driver.find_elements(By.XPATH, "//td[1]")
    num = len(rows)
    print(num)

    for row in rows:
        print("Name:", row.text)

    try:
        if num > 0:
            print(True)
        else:
            print(False)
    except:
        print("exception\n")

    driver.quit()
