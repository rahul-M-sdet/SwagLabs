from selenium import webdriver
from selenium.webdriver.common.by import By


class CheckOutPage:
    button_Check_xpath = "//button[@id='checkout']"
    textbox_FirstName_id = "first-name"
    textbox_LastName_id = "last-name"
    textbox_Zip_xpath = "//input[@id='postal-code']"
    button_continue_id = "continue"
    button_cancel_id = "cancel"
    button_finish_id = "finish"
    button_BacKHome_id = "back-to-products"

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.XPATH, self.button_Check_xpath).click()

    def setFirstName(self):
        self.driver.find_element(By.ID, self.textbox_FirstName_id).clear()
        self.driver.find_element(By.ID, self.textbox_FirstName_id).send_keys("Rahul")

    def setLastName(self):
        self.driver.find_element(By.ID, self.textbox_LastName_id).clear()
        self.driver.find_element(By.ID, self.textbox_LastName_id).send_keys("Mishra")

    def setZIP(self):
        self.driver.find_element(By.XPATH, self.textbox_Zip_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_Zip_xpath).send_keys("482002")

    def clickContinue(self):
        self.driver.find_element(By.ID, self.button_continue_id).click()

    def clickFinish(self):
        self.driver.find_element(By.ID, self.button_finish_id).click()

    def clickHome(self):
        self.driver.find_element(By.ID, self.button_BacKHome_id).click()

    def clickCancel(self):
        self.driver.find_element(By.ID, self.button_cancel_id).click()
