from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class LoginPage(BasePage):
    link_login_id = "loginLink"
    textbox_username_id = "mob_email_id"
    btn_continue_id = "mob_continue_submit"
    textbox_password_xpath = "//input[@id='mob_password']"
    btn_logintoaccount_xpath = "//button[@id='mob_continue_submit']"
    # icon_usericon_xpath = "//i[@class='icon_user']"

    LOGINLINK = (By.ID, "loginLink")
    EMAIL = (By.ID, "mob_email_id")
    ContinueBtn = (By.ID, "mob_continue_submit")
    PASSWORD = (By.XPATH, "//input[@id='mob_password']")
    LOGINBTN = (By.XPATH, "//button[@id='mob_continue_submit']")
    icon_usericon_xpath = (By.XPATH, "//i[@class='icon_user']")


    def __init__(self, driver):
        super().__init__(driver)

    """Login Page Actions"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    def clickOnLoginlink(self):
        self.do_click(self.LOGINLINK)

    def enterUsername(self,username):
        self.driver.do_send_keys(self.textbox_username_id)

    def clickOnContinueBtn(self):
        self.driver.find_element_by_id(self.btn_continue_id).click()

    def enterPassword(self,password):
        self.driver.do_send_keys(self.textbox_password_xpath)

    def clickOnLoginToAccountBtn(self):
        self.driver.do_click(self.btn_logintoaccount_xpath)

    def userIconDisplayed(self):
        isDisplayed = self.is_eleDisplayed(self.icon_usericon_xpath)
        return isDisplayed

    def do_login(self,username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_click(self.ContinueBtn)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGINBTN)