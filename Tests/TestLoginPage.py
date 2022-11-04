import time

import pytest

import config.credential as cd

from Utilities.common_utilities import CommonUtilities
from Utilities.LoginPageUtilities import LoginPageUtilities
from Locators import HomePageLocators as hpl
from conftest import driver


@pytest.mark.usefixtures('initiate_driver')
class TestLoginPage:

    @pytest.mark.validlogin
    def test_verify_login_with_correct_pswrd(self):
        lpu = LoginPageUtilities()
        lpu.click_account()
        lpu.click_login_signup()
        lpu.enter_mobile_num(cd.mobile_num)
        lpu.click_submit()
        time.sleep(20)
        lpu.click_verify_otp()
        assert hpl.search_bar, 'search bar is not displayed'
