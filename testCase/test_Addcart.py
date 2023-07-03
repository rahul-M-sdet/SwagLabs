import time

from selenium.webdriver.common.by import By
from pageObject.LoginPage import loginPage
from pageObject.AddToCart import AddToCart
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_002_AddToCart:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    log2 = LogGen.loggen()

    def test_cartItems(self, setup):
        self.log2.info("********* Verifying Add to cart ********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = loginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()

        self.add2cart = AddToCart(self.driver)
        time.sleep(2)
        self.add2cart.product_click()
        self.msg = self.driver.find_element(By.XPATH,"//div[contains(text(),'Sauce Labs Fleece Jacket')]").text
        time.sleep(2)
        if "Sauce Labs Fleece Jacket" in self.msg:
            self.log2.info("******* verifying product title ************")
            assert True == True
            print("Product is Matched")
        else:
            self.add2cart.remove_click()
            self.add2cart.continueshopping_click()
            self.driver.close()
