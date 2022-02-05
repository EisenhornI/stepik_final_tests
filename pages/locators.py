from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
class LoginPageLocators():
    register_form = (By.CSS_SELECTOR, "#register_form")
    login_form = (By.CSS_SELECTOR, "#login_form")
class ProductPageLocators():
    basket_button = (By.CSS_SELECTOR, ".btn-add-to-basket")
    product_name = (By.CSS_SELECTOR, ".product_main h1")
    added_product_name = (By.CSS_SELECTOR, ".alert-success:nth-child(1) .alertinner strong")
    product_price = (By.CSS_SELECTOR, ".product_main .price_color")
    added_product_price = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    success_message = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
class BasketPageLocators():
    basket_status = (By.CSS_SELECTOR, "#content_inner>p")
    basket_items = (By.CSS_SELECTOR, ".basket-items")