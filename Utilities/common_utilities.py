from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.time_for_wait import explicit_wait_time
from conftest import driver


class CommonUtilities:

    def click_element(self,element):
        WebDriverWait(driver=driver, timeout=explicit_wait_time).\
            until(EC.element_to_be_clickable(element))
        driver.find_element(element[0], element[1]).click()

    def send_text(self, element, text):
        WebDriverWait(driver=driver, timeout=explicit_wait_time).\
            until(EC.presence_of_element_located(element)).send_keys(text)

    def get_text(self, element):
        WebDriverWait(driver=driver, timeout=explicit_wait_time). \
            until(EC.presence_of_element_located(element))

        return driver.find_element(by=element[0], value=element[1]).text

