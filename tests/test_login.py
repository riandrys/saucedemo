import os

import pytest
from saucedemo.pages.login_page import LoginPage
from saucedemo.tests.base_test import BaseTest


class TestLogin(BaseTest):

    @pytest.mark.login
    @pytest.mark.login_success
    def test_login_valid(self):
        login_page = LoginPage(self.driver)
        login_page.set_username("standard_user")
        login_page.set_password("secret_sauce")
        login_page.click_login()
        assert (login_page.get_url() == os.getenv("AFTER_LOGIN_URL"))

