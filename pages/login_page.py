import os

from selenium.webdriver.common.by import By

from saucedemo.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")
        self.open(os.getenv("BASE_URL"))

    def set_username(self, username):
        self.do_send_keys(self.username_field, username)

    def set_password(self, password):
        self.do_send_keys(self.password_field, password)

    def click_login(self):
        self.do_click(self.login_button)

    def login_with_enter(self):
        self.press_enter(self.password_field)

    def error_message_displayed(self):
        return self.is_visible(self.error_message)

    def get_error_message_text(self):
        if self.error_message_displayed():
            return self.get_element_text(self.error_message)
        return None

    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login()
