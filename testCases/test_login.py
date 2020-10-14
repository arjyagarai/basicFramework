import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from commonUtilities.readConfigProperty import Readconfig
from commonUtilities.customLogger import LogHelper
import time

from testCases.test_base import BaseTest


class Test_login_01(BaseTest):
    baseURL = Readconfig.getApplicationUrl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    # cname = Readconfig.getConfigforPayementDetails('customername')
    # cardno = Readconfig.getConfigforPayementDetails('creditcard')

    logger = LogHelper.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self):
        self.logger.info("=====test_homePageTitle======")
        self.logger.info("Verifying HomePageTitle")
        self.lpage = LoginPage(self.driver)
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        exp_title = 'Online Shopping for Men, Women Clothing & Accessories at Bewakoof'
        if act_title == exp_title:
            #self.driver.close()
            self.logger.info("HomePageTitle testcase is passed")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            #self.driver.close()
            self.logger.error("HomePageTitle testcase is failed")
            assert False

    def test_loginToApplication(self):
        self.logger.info("=====test_loginToApplication======")
        self.logger.info("Loging to Application")
        # self.driver.get(self.baseURL)
        # self.lpage = LoginPage(self.driver)
        # self.lpage.clickOnLoginlink()
        # self.logger.info("Clicking on Login link")
        # time.sleep(3)
        # self.lpage.enterUsername(self.username)
        # self.logger.info(f"Entered Username {self.username}")
        # self.lpage.clickOnContinueBtn()
        # self.logger.info("Clicking on Continue button from Username page")
        # time.sleep(3)
        # self.lpage.enterPassword(self.password)
        # self.logger.info("Entered Password")
        # self.lpage.clickOnLoginToAccountBtn()
        # self.logger.info("Clicking on Login button")
        # time.sleep(5)
        self.driver.get(self.baseURL)
        self.lpage = LoginPage(self.driver)
        self.lpage.clickOnLoginlink()
        self.logger.info("Clicking on Login link")
        #time.sleep(5)
        self.lpage.do_login(self.username, self.password)
        self.logger.info(f"Entered Username {self.username}")
        is_displayed = self.lpage.userIconDisplayed()
        assert is_displayed
        self.logger.info("======Execution has been completed=======")



