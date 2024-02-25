import unittest

from selenium import webdriver

from customer_management.lakeside_fetch_customer_seeds import LakeSideFetchProfileSeeds
from customer_management.lakeside_search_customers_seeds import LakesideSearchSeeds


class MyTestCase(unittest.TestCase):
    def test_search_true(self):
        options = webdriver.ChromeOptions()
        options.add_argument('__no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--hide-scrollbars')

        driver = webdriver.Chrome(options=options)

        driver.set_window_size(1920, 967)

        driver.get("http://localhost:3020")

        seed = LakesideSearchSeeds(driver)
        findRes = seed.execute_seeds("a", "Fernande Levicount")

        self.assertEqual(findRes, True)
        driver.quit()

    def test_search_false(self):
        options = webdriver.ChromeOptions()
        options.add_argument('__no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--hide-scrollbars')

        driver = webdriver.Chrome(options=options)

        driver.set_window_size(1920, 967)

        driver.get("http://localhost:3020")

        seed = LakesideSearchSeeds(driver)
        findRes = seed.execute_seeds("a", "ghn")

        self.assertEqual(findRes, False)
        driver.quit()

    def test_fetch_profile(self):
        options = webdriver.ChromeOptions()
        options.add_argument('__no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--hide-scrollbars')

        driver = webdriver.Chrome(options=options)

        driver.set_window_size(1920, 967)

        driver.get("http://localhost:3020")

        seed = LakesideSearchSeeds(driver)
        target = "Fernande Levicount"
        findRes = seed.execute_seeds("a", target)

        self.assertEqual(findRes, True)

        fetchSeed = LakeSideFetchProfileSeeds(driver)
        profile = fetchSeed.execute_seeds(target)

        for key, value in profile.items():
            if key == "Name":
                self.assertEqual(value, "Fernande Levicount")
            elif key == "Address":
                self.assertEqual(value, "45267 Express Alley, 9000 St. Gallen")
            elif key == "Date of Birth":
                self.assertEqual(value, "September 12th 1957")
            elif key == "Email Address":
                self.assertEqual(value, "flevicountw@example.com")
            elif key == "Phone Number":
                self.assertEqual(value, "055 222 4111")


if __name__ == '__main__':
    unittest.main()
