from pageObject.LoginPage import loginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_LoginTitle(self, setup):
        self.logger.info("**************** Veryfying login page ***********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = loginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Swag Labs":
            assert True
            self.logger.info("**************** Login page is passed ***********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_Login.png")
            self.driver.close()
            self.logger.error("**************** Login page is failed ***********")
            assert False
