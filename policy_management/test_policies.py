import random
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from policy_management.lakeside_agreement import Agreement
from policy_management.lakeside_policy_edit_seeds import LakesideEditPolicySeeds
from policy_management.lakeside_policy_fetch_policy_seeds import LakesideFetchPolicySeeds

policy_types = ["Life Insurance", "Home Insurance", "Health Insurance", "Car Insurance"]


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


class MyTestCase(unittest.TestCase):
    def test_edit_policy(self):
        policy_driver = init_policy_service_driver()
        test_username = "Test10001 TestUser"
        # has_policy
        # fetch_seed = LakesideFetchPolicySeeds(policy_driver)
        # edit
        edit_policy_seed = LakesideEditPolicySeeds(policy_driver)
        test_start_date = '2020-12-31'
        test_end_date = '2030-12-31'
        test_policy_type = policy_types[random.randint(0, 3)]
        test_deduct = 100
        test_insurance_premium = 2000
        test_policy_limit = 20000
        edit_policy_seed.execute_seed(test_username, start_date=test_start_date, end_date=test_end_date,
                                      policy_type=test_policy_type,
                                      deduct=test_deduct, insurance_premium=test_insurance_premium,
                                      policy_limit=test_policy_limit,
                                      agreements=[Agreement("test222", "test content222")])

        # jump to policy homepage
        # print("jump to the policy homepage")
        # policy_driver.find_element(By.CSS_SELECTOR, 'a[href="/"]').click()
        # time.sleep(1)
        print("start comparing......")
        get_policy_seed = LakesideFetchPolicySeeds(policy_driver)
        res = get_policy_seed.find_policy()

        self.assertEqual(res["start_date"], test_start_date)
        self.assertEqual(res["end_date"], test_end_date)
        self.assertEqual(res["policy_type"], test_policy_type)
        self.assertEqual(res["deduct"], str(test_deduct)+" CHF")
        self.assertEqual(res["insurance_premium"], str(test_insurance_premium)+" CHF")
        self.assertEqual(res["policy_limit"], str(test_policy_limit)+" CHF")
        print("finish comparing......")
        policy_driver.quit()

if __name__ == '__main__':
    unittest.main()
