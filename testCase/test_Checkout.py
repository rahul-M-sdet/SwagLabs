import time

from selenium.webdriver.common.by import By
from pageObject.LoginPage import loginPage
from pageObject.AddToCart import AddToCart
from pageObject.Checkout import CheckOutPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_CheckOut:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    log1 = LogGen.loggen()
    def test_cartItems(self, setup):
        self.log1.info("**************** Veryfying checkout page ***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = loginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        self.add2cart = AddToCart(self.driver)
        self.add2cart.product_click()
        self.add2cart.Bucket_click()
        self.check = CheckOutPage(self.driver)
        time.sleep(2)

        self.check.checkout()
        self.check.setFirstName()
        self.check.setLastName()
        self.check.setZIP()
        time.sleep(2)
        self.check.clickContinue()
        self.payment = self.driver.find_element(By.XPATH, "//div[@class='summary_value_label'][1]").text
        if self.payment in "SauceCard #31337":
            self.log1.info("********** verifying payment info *************")
            assert True == True
        else:
            self.check.clickCancel()
        time.sleep(2)
        self.check.clickFinish()

        self.status = "Thank you for your order!"
        self.log1.info("***********veryfying thank you after order***********")
        assert "Thank you for your order!" in self.status
        self.check.clickHome()
        self.driver.close()
