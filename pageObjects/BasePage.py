from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
This call will be Parent class of all Page classes
"""

class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def do_click(self,by_locator):
        print(by_locator)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self,by_locator,text_to_enter):
        print(by_locator,text_to_enter)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text_to_enter)

    def get_element_text(self,by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return ele.text

    def is_eleEnabled(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return ele.is_enabled()

    def is_eleDisplayed(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return ele.is_displayed()

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title