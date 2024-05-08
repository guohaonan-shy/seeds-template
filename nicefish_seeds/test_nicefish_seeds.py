import random
import time
import unittest

from nicefish_seeds.comment_seeds import NicefishCommentSeeds
from nicefish_seeds.login_seeds import NicefishLoginSeeds
from nicefish_seeds.signup_seeds import NicefishSignUpSeeds
from nicefish_seeds.utils import init_nicefish_driver
from nicefish_seeds.write_post_seeds import NicefishWritePostSeeds


class MyTestCase(unittest.TestCase):
    def test_signup(self):
        driver = init_nicefish_driver()
        # sign up
        register_seed = NicefishSignUpSeeds(driver)
        test_register_email = "testUserCase{}@example.com".format(random.randint(0, 10000))
        print("email: ", test_register_email)
        test_password = random.randint(10000000, 99999999)
        print("password: ", test_password)
        register_seed.execute_seeds(test_register_email, test_password)
        time.sleep(1)

        driver.quit()

    def test_loginin(self):
        driver = init_nicefish_driver()
        # sign in
        login_seed = NicefishLoginSeeds(driver)

        # jump to the sign-in page
        login_seed.jump_from_home()

        test_user_email = "TestUser@123.com"
        test_password = "12345678"
        login_seed.execute_seeds(test_user_email, test_password)
        time.sleep(1)

        driver.quit()

    def test_register_and_login(self):
        driver = init_nicefish_driver()

        register_seed = NicefishSignUpSeeds(driver)
        test_register_email = "testUserCase{}@example.com".format(random.randint(0, 10000))
        print("email: ", test_register_email)
        test_password = random.randint(10000000, 99999999)
        print("password: ", test_password)
        register_seed.execute_seeds(test_register_email, test_password)
        time.sleep(1)

        # after signing up, the service will jump to the sign-in page automatically
        login_seed = NicefishLoginSeeds(driver)

        login_seed.execute_seeds(test_register_email, test_password)
        time.sleep(1)

        driver.quit()

    def test_write_post(self):
        driver = init_nicefish_driver()

        write_post_seeds = NicefishWritePostSeeds(driver)
        write_post_seeds.jump_to_write_post()
        # because we haven't logged in yet, we will redirect to the sign-in page
        login_seed = NicefishLoginSeeds(driver)
        login_seed.execute_seeds("TestUser@123.com", "12345678")
        # after logging in, we will direct back to the home page
        write_post_seeds.jump_to_write_post()
        # edit
        write_post_seeds.execute_seeds(material_path="./static_material/test_image.jpeg", description="write a post about a cartoon character")

        driver.quit()

    def test_comment_post(self):
        driver = init_nicefish_driver()

        # because we haven't logged in yet, we will redirect to the sign-in page
        login_seed = NicefishLoginSeeds(driver)
        login_seed.jump_from_home()
        login_seed.execute_seeds("TestUser001@123.com", "12345678")
        # after logging in, we will direct back to the home page
        comment_post_seeds = NicefishCommentSeeds(driver)
        comment_post_seeds.jump_to_detail()
        # edit
        comment_post_seeds.execute_seeds(comment='fantastic !!!!')

        driver.quit()