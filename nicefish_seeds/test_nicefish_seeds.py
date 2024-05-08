import random
import time
import unittest

from nicefish_seeds.signup_seeds import NicefishSignUpSeeds
from nicefish_seeds.utils import init_nicefish_driver


class MyTestCase(unittest.TestCase):
    def test_signup(self):
        driver = init_nicefish_driver()
        # register
        register_seed = NicefishSignUpSeeds(driver)
        test_register_email = "testUserCase{}@example.com".format(random.randint(0, 10000))
        print("email: ", test_register_email)
        test_password = random.randint(10000000, 99999999)
        print("password: ", test_password)
        register_seed.execute_seeds(test_register_email, test_password)
        time.sleep(1)

        driver.quit()