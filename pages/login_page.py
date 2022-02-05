from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert("login".find(self.url))

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not presented"
        
    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.register_form), "Register form is not presented"
        
    def register_new_user(self, email, password):
        register_form_adress = self.browser.find_element(*LoginPageLocators.register_form_adress)
        register_form_adress.send_keys(email)
        register_form_password = self.browser.find_element(*LoginPageLocators.register_form_password)
        register_form_password.send_keys(password)
        register_form_password_repeat = self.browser.find_element(*LoginPageLocators.register_form_password_repeat)
        register_form_password_repeat.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.register_button)
        register_button.click()

