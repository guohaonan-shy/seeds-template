import random
import time
import unittest

from nicefish_seeds.access_writer_info_seeds import NicefishAccessWriterSeeds
from nicefish_seeds.collect_seeds import NicefishCollectSeeds
from nicefish_seeds.comment_seeds import NicefishCommentSeeds
from nicefish_seeds.follow_seeds import NicefishFollowSeeds
from nicefish_seeds.like_seeds import NicefishLikeSeeds
from nicefish_seeds.login_seeds import NicefishLoginSeeds
from nicefish_seeds.profile_seeds import NicefishProfileSeeds
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
        write_post_seeds.execute_seeds(material_path="./static_material/test_image.jpeg",
                                       description="write a post about a cartoon character")

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

    def test_follow_writer(self):
        driver = init_nicefish_driver()

        # because we haven't logged in yet, we will redirect to the sign-in page
        login_seed = NicefishLoginSeeds(driver)
        login_seed.jump_from_home()
        login_seed.execute_seeds("TestUser001@123.com", "12345678")

        follow_seed = NicefishFollowSeeds(driver)
        follow_cnt = follow_seed.get_current_follows()

        follow_seed.jump_to_detail()

        follow_seed.execute_seeds()

        new_cnt = follow_seed.get_current_follows()

        self.assertEqual(follow_cnt + 1, new_cnt)

    def test_like_poster(self):
        driver = init_nicefish_driver()
        login_seed = NicefishLoginSeeds(driver)
        login_seed.jump_from_home()
        login_seed.execute_seeds("TestUser001@123.com", "12345678")

        # get the like count before click
        driver1 = init_nicefish_driver()
        login_seed1 = NicefishLoginSeeds(driver1)
        login_seed1.jump_from_home()
        login_seed1.execute_seeds("TestUser001@123.com", "12345678")

        user_home_seed = NicefishAccessWriterSeeds(driver1)
        user_home_seed.jump_from_homepage()
        before_cnt = user_home_seed.get_likes()
        # execute like operation
        like_seed = NicefishLikeSeeds(driver)

        like_seed.jump_to_detail()

        like_seed.execute_seeds()
        # check
        driver1.refresh()
        time.sleep(1)
        after_cnt = user_home_seed.get_likes()

        self.assertEqual(before_cnt + 1, after_cnt)

    def test_collect_poster(self):
        driver = init_nicefish_driver()
        login_seed = NicefishLoginSeeds(driver)
        login_seed.jump_from_home()
        login_seed.execute_seeds("TestUser001@123.com", "12345678")

        # execute like operation
        collect_seed = NicefishCollectSeeds(driver)

        collect_seed.jump_to_detail(target_post_id=57)

        # get the collection before click
        driver1 = init_nicefish_driver()
        login_seed1 = NicefishLoginSeeds(driver1)
        login_seed1.jump_from_home()
        login_seed1.execute_seeds("TestUser001@123.com", "12345678")

        user_home_seed = NicefishAccessWriterSeeds(driver1)
        user_home_seed.jump_from_homepage()
        before_collect_status = user_home_seed.get_targeted_collection(target_post_id=57)
        self.assertEqual(before_collect_status, False)
        # execute
        collect_seed.execute_seeds()

    def test_update_profile(self):
        driver = init_nicefish_driver()
        login_seed = NicefishLoginSeeds(driver)
        login_seed.jump_from_home()
        login_seed.execute_seeds("TestUser001@123.com", "12345678")

        profile_seed = NicefishProfileSeeds(driver)
        profile_seed.jump_to_profile()

        avatar = "./static_material/test_avatar.png"
        nickname = "lucky dog"
        remark = "here is a dog......"

        profile_seed.execute_seeds(avatar=avatar, nickname=nickname, remark=remark)
