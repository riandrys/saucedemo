import allure
import pytest
import requests

from saucedemo.config.settings import settings
from saucedemo.pages.login_page import LoginPage
from saucedemo.pages.product_list_page import ProductListPage
from saucedemo.tests.base_test import BaseTest


class TestProductListPage(BaseTest):
    @pytest.mark.product_page
    @allure.feature("Product List Page Feature")
    @allure.story("Get list of products from PLP")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_products(self):
        login_page = LoginPage(self.driver)
        login_page.login(settings.username, settings.password)
        product_page = ProductListPage(self.driver)
        product_names = product_page.get_list_of_product_names()
        assert len(product_names) > 0, "No products found on the PLP."

    @pytest.mark.product_page
    @pytest.mark.product_sort
    @allure.feature("Product List Page Feature")
    @allure.story("Sort products in alphabetical order")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sort_a_to_z(self):
        login_page = LoginPage(self.driver)
        login_page.login(settings.username, settings.password)
        product_page = ProductListPage(self.driver)
        product_page.sort_products_a_to_z()
        product_names = product_page.get_list_of_product_names()
        for i in range(len(product_names) - 1):
            assert (
                product_names[i] <= product_names[i + 1]
            ), "Products {0} and {1} are not ordered correctly.".format(
                product_names[i], product_names[i + 1]
            )

    @pytest.mark.product_page
    @pytest.mark.product_sort
    @allure.feature("Product List Page Feature")
    @allure.story("Sort products in reverse alphabetical order")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sort_z_to_a(self):
        login_page = LoginPage(self.driver)
        login_page.login(settings.username, settings.password)
        product_page = ProductListPage(self.driver)
        product_page.sort_products_z_to_a()
        product_names = product_page.get_list_of_product_names()
        for i in range(len(product_names) - 1):
            assert (
                product_names[i] >= product_names[i + 1]
            ), "Products {0} and {1} are not ordered correctly.".format(
                product_names[i], product_names[i + 1]
            )

    @pytest.mark.product_page
    @pytest.mark.product_sort
    @allure.feature("Product List Page Feature")
    @allure.story("Sort products by price in ascending order")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sort_low_to_high_by_price(self):
        login_page = LoginPage(self.driver)
        login_page.login(settings.username, settings.password)
        product_page = ProductListPage(self.driver)
        product_page.sort_products_low_to_high()
        product_prices = product_page.get_list_of_product_prices()
        for i in range(len(product_prices) - 1):
            assert (
                product_prices[i] <= product_prices[i + 1]
            ), "Products {0} and {1} are not ordered correctly.".format(
                product_prices[i], product_prices[i + 1]
            )

    @pytest.mark.product_page
    @pytest.mark.product_sort
    @allure.feature("Product List Page Feature")
    @allure.story("Sort products by price in descending order")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sort_high_to_low_by_price(self):
        login_page = LoginPage(self.driver)
        login_page.login(settings.username, settings.password)
        product_page = ProductListPage(self.driver)
        product_page.sort_products_high_to_low()
        product_prices = product_page.get_list_of_product_prices()
        for i in range(len(product_prices) - 1):
            assert (
                product_prices[i] >= product_prices[i + 1]
            ), "Products {0} and {1} are not ordered correctly.".format(
                product_prices[i], product_prices[i + 1]
            )

    @pytest.mark.product_page
    @pytest.mark.add_to_cart
    @allure.feature("Product List Page Feature")
    @allure.story("Add product to cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_product_to_cart(self):
        login_page = LoginPage(self.driver)
        login_page.login(settings.username, settings.password)
        product_page = ProductListPage(self.driver)
        product_elements = product_page.get_all_product_elements()

        num_items_in_cart = 0
        assert (
            product_page.get_number_cart_items() == num_items_in_cart
        ), "An unexpected item has been found in the cart."

        num_items_in_cart = product_page.get_number_cart_items()

        for product_element in product_elements:
            product_page.add_product_to_cart(product_element)
            num_items_in_cart += 1
            assert (
                product_page.get_number_cart_items() == num_items_in_cart
            ), "Product {0} has not been added to the cart.".format(
                product_element.text
            )

            assert (
                product_page.get_button_add_to_cart_text(product_element) == "Remove"
            ), "Button not changed to 'Remove' for product {0}".format(
                product_element.text
            )

    @pytest.mark.product_page
    @pytest.mark.remove_from_cart
    @allure.feature("Product List Page Feature")
    @allure.story("Remove product from cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_product_from_cart(self):
        login_page = LoginPage(self.driver)
        login_page.login(settings.username, settings.password)
        product_page = ProductListPage(self.driver)
        product_elements = product_page.get_all_product_elements()

        num_items_in_cart = 0
        assert (
            product_page.get_number_cart_items() == num_items_in_cart
        ), "An unexpected item has been found in the cart."
        product_page.add_all_to_cart()
        num_items_in_cart = product_page.get_number_cart_items()

        for product_element in product_elements:
            product_page.remove_product_from_cart(product_element)
            num_items_in_cart -= 1
            assert (
                product_page.get_number_cart_items() == num_items_in_cart
            ), "Product {0} has not been removed from the cart.".format(
                product_element.text
            )

            assert (
                product_page.get_button_add_to_cart_text(product_element)
                == "Add to cart"
            ), "Button not changed to 'Add to cart' for product {0}".format(
                product_element.text
            )

    @pytest.mark.product_page
    @pytest.mark.plp_images
    @allure.feature("Product List Page Feature")
    @allure.story("Test that each product's image link is not broken.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_plp_images(self):
        login_page = LoginPage(self.driver)
        login_page.login(settings.username, settings.password)
        product_page = ProductListPage(self.driver)
        product_elements = product_page.get_all_product_elements()
        broken_image_count = 0
        for product in product_elements:
            image_src = product_page.get_image_src(product)
            try:
                response = requests.get(image_src, stream=True)
                if response.status_code != 200:
                    print(
                        "Encountered status code {0} when trying to access {1}".format(
                            response.status_code, image_src
                        )
                    )
                    broken_image_count += 1
            except requests.exceptions.MissingSchema:
                print("Encountered MissingSchema Exception")
            except requests.exceptions.InvalidSchema:
                print("Encountered InvalidSchema Exception")
            except requests.exceptions.RequestException:
                print("Encountered Some other Exception")

        assert broken_image_count == 0, "Broken image count is {0}".format(
            broken_image_count
        )
