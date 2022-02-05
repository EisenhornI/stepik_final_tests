from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.basket_status), "Basket is not empty"
    def should_not_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.basket_status), "Basket is empty"
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.basket_items), "Items are there, but should not be"