from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.basket_button)
        basket_button.click()
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    def check_added_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.product_name).text
        added_product_name = self.browser.find_element(*ProductPageLocators.added_product_name).text
        assert product_name == added_product_name, "Added product name does not match "
    def check_added_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.product_price).text
        added_product_price = self.browser.find_element(*ProductPageLocators.added_product_price).text
        assert product_price == added_product_price, "The price of the added product does not match "