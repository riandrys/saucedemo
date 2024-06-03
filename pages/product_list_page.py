from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

from saucedemo.pages.base_page import BasePage


class ProductListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_button_selector = (By.CLASS_NAME, "btn_primary")
        self.remove_from_cart_button_selector = (By.CLASS_NAME, "btn_secondary")
        self.add_to_cart_or_remove_button_selector = (By.CLASS_NAME, "btn_inventory")
        self.hamburger_menu_selector = (By.ID, "react-burger-menu-btn")
        self.cart_item_count_selector = (
            By.CSS_SELECTOR,
            "[data-test='shopping-cart-badge']",
        )
        self.cart_selector = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
        self.inventory_item_names_selector = (
            By.CSS_SELECTOR,
            "[data-test='inventory-item-name']",
        )
        self.inventory_item_prices_selector = (
            By.CSS_SELECTOR,
            "[data-test='inventory-item-price']",
        )
        self.inventory_items_selector = (
            By.CSS_SELECTOR,
            "[data-test='inventory-item']",
        )
        self.sort_menu_selector = (
            By.CSS_SELECTOR,
            "select[data-test='product-sort-container']",
        )
        self.product_image_selector = (By.XPATH, ".//div[1]/a/img")
        self.product_link_selector = (
            By.CSS_SELECTOR,
            ".inventory_item .inventory_item_description a",
        )

    def click_cart(self):
        self.do_click(self.cart_selector)

    def click_hamburger_menu(self):
        self.do_click(self.hamburger_menu_selector)

    def get_add_to_cart_buttons(self):
        buttons = self.get_elements(self.add_to_cart_button_selector)
        return buttons

    def get_all_product_elements(self):
        products = self.get_elements(self.inventory_items_selector)
        return products

    def get_list_of_product_names(self):
        products = self.get_elements(self.inventory_item_names_selector)
        return [item.text for item in products]

    def get_number_cart_items(self):
        has_items_in_cart = self.is_present(self.cart_item_count_selector)
        if has_items_in_cart:
            num_items_in_cart = self.get_element(self.cart_item_count_selector).text
            return int(num_items_in_cart)
        return 0

    def get_list_of_product_prices(self):
        products = self.get_elements(self.inventory_item_prices_selector)
        return [float(item.text.replace("$", "")) for item in products]

    def sort_products_a_to_z(self):
        select = Select(self.get_element(self.sort_menu_selector))
        select.select_by_value("az")

    def sort_products_low_to_high(self):
        select = Select(self.get_element(self.sort_menu_selector))
        select.select_by_value("lohi")

    def sort_products_high_to_low(self):
        select = Select(self.get_element(self.sort_menu_selector))
        select.select_by_value("hilo")

    def sort_products_z_to_a(self):
        select = Select(self.get_element(self.sort_menu_selector))
        select.select_by_value("za")

    def add_all_to_cart(self):
        product_elements = self.get_all_product_elements()
        for product in product_elements:
            self.add_product_to_cart(product)

    def add_product_to_cart(self, product: WebElement):
        add_cart_button = product.find_element(*self.add_to_cart_button_selector)
        add_cart_button.click()

    def remove_product_from_cart(self, product: WebElement):
        remove_cart_button = product.find_element(
            *self.remove_from_cart_button_selector
        )
        remove_cart_button.click()

    def get_button_add_to_cart_text(self, product: WebElement):
        return product.find_element(*self.add_to_cart_or_remove_button_selector).text

    def get_image_src(self, product: WebElement):
        return product.find_element(*self.product_image_selector).get_attribute("src")

    def get_product_name(self, product: WebElement):
        return product.find_element(*self.inventory_item_names_selector).text

    def get_product_price(self, product: WebElement):
        return product.find_element(*self.inventory_item_prices_selector).text

    def get_product_by_name(self, name: str):
        products = self.get_all_product_elements()
        for product in products:
            product_name = self.get_product_name(product)
            if product_name == name:
                return product
        return None

    def get_product_link(self, product: WebElement):
        return product.find_element(*self.product_link_selector).get_attribute("href")

    def open_product_detail(self, product: WebElement):
        product.find_element(*self.product_link_selector).click()
