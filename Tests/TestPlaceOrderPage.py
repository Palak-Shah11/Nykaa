import time

import pytest

import config.credential as cd

from Utilities.common_utilities import CommonUtilities
from Utilities.LoginPageUtilities import LoginPageUtilities
from Locators import HomePageLocators as hpl
from conftest import driver


class TestLoginPage:
    @pytest.mark.usefixtures('initiate_driver')
    def test_verify_to_place_order(self):
        lpu = LoginPageUtilities()
        lpu.click_account()
        lpu.click_login_signup()
        lpu.enter_mobile_num(cd.mobile_num)
        lpu.click_submit()
        time.sleep(20)
        lpu.click_verify_otp()
        lpu.fill_search_product(cd.search_product)
        # driver.implicitly_wait(10)
        time.sleep(5)
        lpu.click_product()
        lpu.click_product_img()
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        lpu.click_size()
        lpu.click_add_to_bag()
        lpu.click_view_bag()
        driver.switch_to.frame(driver.find_element(hpl.iframe_locator[0], hpl.iframe_locator[1]))
        time.sleep(5)
        lpu.click_got_it_btn()
        lpu.click_proceed_to_buy()
        lpu.click_proceed_to_pay()
        time.sleep(10)

    @pytest.mark.usefixtures('initiate_driver')
    def test_verify_item_saved_to_wishlist(self):
        lpu = LoginPageUtilities()
        lpu.click_account()
        lpu.click_login_signup()
        lpu.enter_mobile_num(cd.mobile_num)
        lpu.click_submit()
        time.sleep(20)
        lpu.click_verify_otp()
        lpu.fill_search_product(cd.search_product)
        # driver.implicitly_wait(10)
        time.sleep(5)
        lpu.click_product()
        lpu.click_product_img()
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        lpu.click_size()
        lpu.click_add_to_bag()
        lpu.click_view_bag()
        driver.switch_to.frame(driver.find_element(hpl.iframe_locator[0], hpl.iframe_locator[1]))
        time.sleep(5)
        lpu.click_move_to_wishlist()
        time.sleep(10)
        lpu.click_back_to_shopping()
        time.sleep(10)
        driver.switch_to.default_content()
        lpu.click_element(element=hpl.wishlist)
        time.sleep(10)
        print(tabs)
        driver.switch_to.window(tabs[0])

        print(driver.current_url)
        driver.switch_to.window(tabs[1])

        print(driver.current_url)
        # lpu.find_product_in_whishList()


