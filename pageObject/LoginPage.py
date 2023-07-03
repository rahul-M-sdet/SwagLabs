from selenium.webdriver.common.by import By


class loginPage:
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_login_name_xpath = "//input[@name='login-button']"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_name_xpath).click()
