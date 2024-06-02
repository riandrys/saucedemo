import json
import pytest
import allure

from saucedemo.config.settings import settings
from saucedemo.pages.login_page import LoginPage
from saucedemo.tests.base_test import BaseTest


class TestLogin(BaseTest):
    with open(settings.credentials_file) as f:
        credentials = json.load(f)

    @pytest.mark.login
    @pytest.mark.login_success
    @allure.feature("Login Feature")
    @allure.story("Login with valid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_valid(self):
        valid_user_credentials = self.credentials.get("valid_user_credentials")

        login_page = LoginPage(self.driver)
        login_page.set_username(valid_user_credentials.get("username"))
        login_page.set_password(valid_user_credentials.get("password"))
        login_page.click_login()
        assert login_page.get_url() == settings.after_login_url

    @pytest.mark.login
    @pytest.mark.login_lockedout
    @allure.feature("Login Feature")
    @allure.story("Login with locked out user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_locked_out(self):
        locked_out_user = self.credentials.get("locked_out_user")

        login_page = LoginPage(self.driver)
        login_page.set_username(locked_out_user.get("username"))
        login_page.set_password(locked_out_user.get("password"))
        login_page.click_login()
        assert login_page.get_error_message_text() == "Epic sadface: Sorry, this user has been locked out."

    @pytest.mark.parametrize(
        "username, password",
        [
            (c["username"], c["password"])
            for c in [
                *credentials.get("invalid_user_name"),
                *credentials.get("invalid_password"),
                *credentials.get("invalid_user_name_and_password")
            ]
        ]
    )
    @pytest.mark.login
    @pytest.mark.login_incorrect
    @allure.feature("Login Feature")
    @allure.story("Login with invalid credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_incorrect(self, username, password):
        login_page = LoginPage(self.driver)
        login_page.set_username(username)
        login_page.set_password(password)
        login_page.click_login()
        assert login_page.get_error_message_text() == "Epic sadface: Username and password do not match any user in this service"