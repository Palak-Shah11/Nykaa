import config.credential as cd

from Utilities.common_utilities import CommonUtilities
import Locators.LoginPageLocators as lpl
import Locators.HomePageLocators as hpl
from conftest import driver


class LoginPageUtilities(CommonUtilities):

    def click_account(self):
        self.click_element(lpl.account_btn)

    def click_login_signup(self):
        self.click_element(lpl.login_signup_btn)

    def enter_mobile_num(self, mobilenum):
        self.send_text(lpl.enter_mobile_num, mobilenum)

    def click_submit(self):
        self.click_element(lpl.submit_btn)

    def click_verify_otp(self):
        self.click_element(lpl.verify_otp)

    def fill_search_product(self, productname):
        self.send_text(hpl.search_bar, productname)

    def click_product(self):
        self.click_element(hpl.product_name)

    def click_product_img(self):
        self.click_element(hpl.product_img)

    def click_size(self):
        self.click_element(hpl.size_s)

    def click_add_to_bag(self):
        self.click_element(hpl.add_to_bag)

    def click_view_bag(self):
        self.click_element(hpl.view_bag)

    def click_proceed_to_buy(self):
        self.click_element(hpl.proceed_to_buy)

    def click_got_it_btn(self):
        self.click_element(hpl.got_it_button_iframe)

    def click_proceed_to_pay(self):
        self.click_element(hpl.proceed_to_pay)

    def click_move_to_wishlist(self):
        self.click_element(hpl.move_to_wishlist)

    def click_back_to_shopping(self):
        self.click_element(hpl.back_to_shopping)

    def find_product_in_whishList(self, element):

        lst = driver.find_elements(by=element[0], value=element[1])

        for i in lst:
            print(i.text)

