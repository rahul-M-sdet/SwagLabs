from selenium.webdriver.common.by import By
from selenium import webdriver


class AddToCart:

    def __init__(self, driver):
        self.driver = driver

    button_addToCart_xpath = " //button[@id='add-to-cart-sauce-labs-fleece-jacket'] "
    button_Remove_xpath = "//button[@id='remove-sauce-labs-fleece-jacket']"
    button_continue_id = "continue-shopping"
    link_button_xpath = "//a[@class='shopping_cart_link']"

    def product_click(self):
        self.driver.find_element(By.XPATH, self.button_addToCart_xpath).click()

    def remove_click(self):
        self.driver.find_element(By.XPATH, self.button_Remove_xpath).click()

    def continueshopping_click(self):
        self.driver.find_element(By.ID, self.button_continue_id).click()

    def Bucket_click(self):
        self.driver.find_element(By.XPATH, self.link_button_xpath).click()