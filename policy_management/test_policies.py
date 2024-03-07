import random
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from policy_management.lakeside_agreement import Agreement
from policy_management.lakeside_policy_customer_management_seeds import LakesidePolicyCustomerManagementSeeds
from policy_management.lakeside_policy_edit_seeds import LakesideEditPolicySeeds
from policy_management.lakeside_policy_fetch_policy_seeds import LakesideFetchPolicySeeds
from policy_management.lakeside_respond_quote_request_seeds import LakesideRespondQuoteRequestSeeds

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
        self.assertEqual(res["deduct"], str(test_deduct) + " CHF")
        self.assertEqual(res["insurance_premium"], str(test_insurance_premium) + " CHF")
        self.assertEqual(res["policy_limit"], str(test_policy_limit) + " CHF")
        print("finish comparing......")
        policy_driver.quit()

    def test_respond(self):
        policy_driver = init_policy_service_driver()
        test_username = "Test10001 TestUser"
        respond_seed = LakesideRespondQuoteRequestSeeds(policy_driver)
        respond_seed.jump_to_quote_request()
        target_policy_id = respond_seed.execute_seeds(test_username)
        respond_seed.jump_to_quote_request()
        items = policy_driver.find_elements(By.XPATH, '/html/body/div/div[2]/div/table[1]/tbody/tr')
        for item in items:
            columns = item.find_elements(By.CSS_SELECTOR, 'td')
            detail_button = columns[4].find_element(By.CSS_SELECTOR, 'a[class="ui compact small button"]')
            policy_id = detail_button.get_attribute("href").split('/')[-1]
            if policy_id == target_policy_id:
                print("policy_id:{},assert".format(policy_id))
                status = columns[3].find_element(By.CSS_SELECTOR, 'i').text
                self.assertEqual(status, "Waiting for Customer response")
                return

        policy_driver.quit()

    def test_search_true(self):
        policy_driver = init_policy_service_driver()
        test_condition = "Test10001"
        test_target = "Test10001 TestUser"
        customer_seeds = LakesidePolicyCustomerManagementSeeds(policy_driver)
        customer_seeds.jump_to_customer()
        uid = customer_seeds.search(test_condition, test_target)
        self.assertEqual(uid, "2nuil03wfo")

        policy_driver.quit()

    def test_search_false(self):
        policy_driver = init_policy_service_driver()
        test_condition = "sdasd"
        test_target = "Test10001 TestUser"
        customer_seeds = LakesidePolicyCustomerManagementSeeds(policy_driver)
        customer_seeds.jump_to_customer()
        uid = customer_seeds.search(test_condition, test_target)
        self.assertEqual(uid, None)

        policy_driver.quit()

    def test_create_policy_from_policy_management(self):
        policy_driver = init_policy_service_driver()
        test_condition = "Test10001"
        test_target = "Test10001 TestUser"
        customer_seeds = LakesidePolicyCustomerManagementSeeds(policy_driver)
        customer_seeds.jump_to_customer()



        uid = customer_seeds.search(test_condition, test_target)

        customer_seeds.click_risk_factor()
        score = customer_seeds.get_risk_factor()

        if score >= 50:
            print("score more than 50, add new policy for this user......")

            test_start_date = '2020-12-31'
            test_end_date = '2030-12-31'
            test_policy_type = policy_types[random.randint(0, 3)]
            test_deduct = 200
            test_insurance_premium = 3000
            test_policy_limit = 50000

            customer_seeds.create_new_policy(start_date=test_start_date, end_date=test_end_date,
                                             policy_type=test_policy_type,
                                             deduct=test_deduct, insurance_premium=test_insurance_premium,
                                             policy_limit=test_policy_limit,
                                             agreements=[Agreement("test title",
                                                                   "test content created from policy management")])
        else:
            print("score less than 50, don't add new policy for this user......")


if __name__ == '__main__':
    unittest.main()
