from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage


class MenPage(BasePage):
    MENLINK = (By.LINK_TEXT, "MEN")
    linktxt_size_link = "M"
    #img_Tshirt_xpath = "//img[@title='Hey There Imposter Half Sleeve T-Shirt Neon Green-Front Bewakoof']"
    img_Tshirt_xpath =  "//img[contains(@title,'Half Sleeve T-Shirt Neon')]"

    def __init__(self, driver):
        super().__init__(driver)

    def clickOnMenLink(self):
        self.do_click(self.MENLINK)

    def filterWithSize(self):
        self.driver.find_element_by_link_text(self.linktxt_size_link).click()

    def clickOnTShirt(self):
        self.driver.find_element_by_xpath(self.img_Tshirt_xpath).click()


