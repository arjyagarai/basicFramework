import pytest
from commonUtilities.customLogger import LogHelper
from commonUtilities.readConfigProperty import Readconfig
from pageObjects.MenPage import MenPage
from pageObjects.LoginPage import LoginPage
import time

from testCases.test_base import BaseTest


class Test_MenPage(BaseTest):
    baseURL = Readconfig.getApplicationUrl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    logger = LogHelper.loggen()
    @pytest.mark.sanity
    def test_Testcase001(self):
        self.logger.info("Loging to Application")
        self.driver.get(self.baseURL)
        self.lpage = LoginPage(self.driver)
        self.lpage.clickOnLoginlink()
        self.logger.info("Clicking on Login link")
        # time.sleep(5)
        self.lpage.do_login(self.username, self.password)
        self.logger.info(f"Entered Username {self.username}")

        self.mPage = MenPage(self.driver)
        self.mPage.clickOnMenLink()
        self.logger.info("Clicking on Men Link")

    @pytest.mark.skip("This functionality is not developed")
    def test_one(self):
        pass

    def test_two(self):
        self.logger.info("test_two")