import allure
import pytest
import requests

from saucedemo.config.settings import settings
from saucedemo.pages.login_page import LoginPage
from saucedemo.pages.product_detail_page import ProductDetailPage
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
        if product_page.get_number_cart_items() != num_items_in_cart:
            print("Cart is not empty.")

        num_items_in_cart = product_page.get_number_cart_items()

        not_added_to_cart = 0
        not_changed_to_remove = 0

        for product_element in product_elements:
            product_page.add_product_to_cart(product_element)
            num_items_in_cart += 1
            product_name = product_page.get_product_name(product_element)

            if product_page.get_number_cart_items() != num_items_in_cart:
                print(
                    "Product {0} has not been added to the cart.\n".format(product_name)
                )
                not_added_to_cart += 1
                num_items_in_cart = product_page.get_number_cart_items()
            if product_page.get_button_add_to_cart_text(product_element) != "Remove":
                print(
                    "Button not changed to 'Remove' for product {0}.\n".format(
                        product_name
                    )
                )
                not_changed_to_remove += 1

        assert (
            not_added_to_cart == 0
        ), "{0} Products have not been added to the cart.".format(not_added_to_cart)

        assert (
            not_changed_to_remove == 0
        ), "{0} Products have not been changed to 'Remove'.".format(
            not_changed_to_remove
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
        if product_page.get_number_cart_items() != num_items_in_cart:
            print("Cart is not empty.")
        product_page.add_all_to_cart()
        num_items_in_cart = product_page.get_number_cart_items()

        not_removed_from_cart = 0
        not_changed_to_add = 0

        for product_element in product_elements:
            product_page.remove_product_from_cart(product_element)
            num_items_in_cart -= 1
            product_name = product_page.get_product_name(product_element)

            if product_page.get_number_cart_items() != num_items_in_cart:
                print(
                    "Product {0} has not been removed from the cart.".format(
                        product_name
                    )
                )
                not_removed_from_cart += 1
                num_items_in_cart = product_page.get_number_cart_items()

            if (
                product_page.get_button_add_to_cart_text(product_element)
                != "Add to cart"
            ):
                print(
                    "Button not changed to 'Add to cart' for product {0}".format(
                        product_name
                    )
                )
                not_changed_to_add += 1

        assert (
            not_removed_from_cart == 0
        ), "{0} Products have not been removed from the cart.".format(
            not_removed_from_cart
        )

        assert (
            not not_changed_to_add
        ), "{0} Products have not been changed to 'Add to cart'.".format(
            not_changed_to_add
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

    @pytest.mark.skip(reason="The href value is not working for some reason.")
    @pytest.mark.product_page
    @pytest.mark.plp_links
    @allure.feature("Product List Page Feature")
    @allure.story("Test product list links")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        "Test to ensure that the PLP product link properly redirects to the associated PDP."
    )
    def test_product_list_links(self):
        login_page = LoginPage(self.driver)
        login_page.login(settings.username, settings.password)
        product_page = ProductListPage(self.driver)
        product_elements = product_page.get_all_product_elements()

        product_link_map = {}
        for product in product_elements:
            product_name = product_page.get_product_name(product)
            product_link_map[product_name] = product_page.get_product_link(product)

        bad_links = 0
        for name, link in product_link_map.items():
            self.driver.get(link)
            pdp_page = ProductDetailPage(self.driver)
            pdp_product_name = pdp_page.get_product_name()
            if pdp_product_name != name:
                print("The PLP link for {0} was not correct: {1}".format(name, link))
                bad_links += 1

        assert bad_links == 0, "{0} incorrect links were found on the PLP.".format(
            bad_links
        )

    @pytest.mark.product_page
    @pytest.mark.plp_links
    @allure.feature("Product List Page Feature")
    @allure.story("Test product list links")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        "Test to ensure that the PLP product links properly redirects to the associated PDP."
    )
    def test_plp_links(self):
        login_page = LoginPage(self.driver)
        login_page.login(settings.username, settings.password)
        product_page = ProductListPage(self.driver)
        product_names = product_page.get_list_of_product_names()

        bad_links = 0
        for product_name in product_names:
            product = product_page.get_product_by_name(product_name)
            product_page.open_product_detail(product)

            pdp_page = ProductDetailPage(self.driver)
            pdp_product_name = pdp_page.get_product_name()

            if pdp_product_name != product_name:
                print(
                    "The PLP link for {0} was not correct: {1}".format(
                        product_name, pdp_product_name
                    )
                )
                bad_links += 1
            pdp_page.click_back()

        assert bad_links == 0, "{0} incorrect links were found on the PLP.".format(
            bad_links
        )

    @pytest.mark.product_page
    @pytest.mark.plp_prices
    @allure.feature("Product List Page Feature")
    @allure.story("Test product list prices")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Check that the PLP prices match the PDP prices.")
    def test_plp_prices(self):
        login_page = LoginPage(self.driver)
        login_page.login(settings.username, settings.password)
        product_page = ProductListPage(self.driver)
        product_names = product_page.get_list_of_product_names()

        bad_prices = 0
        for product_name in product_names:
            product = product_page.get_product_by_name(product_name)
            product_price = product_page.get_product_price(product)

            product_page.open_product_detail(product)

            pdp_page = ProductDetailPage(self.driver)
            pdp_price = pdp_page.get_price()

            if pdp_price != product_price:
                print(
                    "The PLP price {0} for {1} not matched with PDP price {2}".format(
                        product_price, product_name, pdp_price
                    )
                )
                bad_prices += 1
            pdp_page.click_back()

        assert bad_prices == 0, "{0} incorrect prices were found on the PLP.".format(
            bad_prices
        )
