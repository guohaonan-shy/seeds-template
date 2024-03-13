import random
import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from customer_self_service.lakeside_insurance_request_seeds import LakesideRequestInsuranceSeeds
from customer_self_service.lakeside_login_seeds import LakesideLoginSeeds
from policy_management.lakeside_agreement import Agreement
from policy_management.lakeside_policy_customer_management_seeds import LakesidePolicyCustomerManagementSeeds
from policy_management.lakeside_policy_delete_seeds import LakesideDeletePolicySeeds
from policy_management.lakeside_policy_edit_seeds import LakesideEditPolicySeeds
from policy_management.lakeside_policy_fetch_policy_seeds import LakesideFetchPolicySeeds
from policy_management.lakeside_respond_quote_request_seeds import LakesideRespondQuoteRequestSeeds
from utils import init_customer_self_service_driver, init_customer_management_service_driver, init_policy_service_driver

policy_types = ["Life Insurance", "Home Insurance", "Health Insurance", "Car Insurance"]


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

        policies = policy_driver.find_elements(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[4]/div')
        old_policies_cnt = len(policies)

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

            new_policies_cnt = len(policy_driver.find_elements(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[4]/div'))
            print("assert is new policies added......")
            self.assertEqual(new_policies_cnt - old_policies_cnt, 1)
        else:
            print("score less than 50, don't add new policy for this user......")

    def test_delete_policy(self):
        policy_driver = init_policy_service_driver()
        table = policy_driver.find_element(By.CSS_SELECTOR, 'table[class="ui celled padded table"]')
        items = table.find_elements(By.XPATH, '//tbody//tr')

        test_target_pid = "0x4hwhnfun"
        for item in items:
            columns = item.find_elements(By.CSS_SELECTOR, 'td')
            show_button = columns[-1].find_element(By.CSS_SELECTOR, 'a')
            pid = show_button.get_attribute("href").split('/')[-1]
            if pid == test_target_pid:
                show_button.click()
                time.sleep(1)
                print("jump to the detail page......")
                delete_seeds = LakesideDeletePolicySeeds(policy_driver)
                delete_seeds.policy_delete(pid)
                break

        items = policy_driver.find_elements(By.XPATH, '/html/body/div/div[2]/div/table/tbody/tr')
        is_find = False
        for item in items:
            columns = item.find_elements(By.CSS_SELECTOR, 'td')
            pid = columns[-1].find_element(By.CSS_SELECTOR, 'a').get_attribute("href").split('/')[-1]
            if pid == test_target_pid:
                is_find = True
                break
        print("assert is delete......")
        self.assertEqual(is_find, False)

    def test_insurance_quote(self):
        customer_driver = init_customer_self_service_driver()
        # login
        login_seed = LakesideLoginSeeds(customer_driver)
        login_seed.execute_seeds(from_signup=False, email="testUserCase6879@example.com", password="744822")

        #
        try:
            requests = customer_driver.find_elements(By.XPATH, '//table[@class="ui selectable table"]//tbody//tr')
        except NoSuchElementException:
            print("there is not requests for this user")
            requests = []

        # request a new quote
        request_insurance_seed = LakesideRequestInsuranceSeeds(customer_driver)
        request_insurance_seed.execute_seeds()
        # process from policy management
        policy_driver = init_policy_service_driver()
        test_username = "User6754 Test"
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
        customer_driver.quit()


if __name__ == '__main__':
    unittest.main()
