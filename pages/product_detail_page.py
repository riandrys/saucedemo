from selenium.webdriver.common.by import By

from saucedemo.pages.base_page import BasePage


class ProductDetailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.price_selector = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
        self.add_to_cart_button_selector = (By.CLASS_NAME, "btn_inventory")
        self.back_button_selector = (By.ID, "back-to-products")
        self.product_name_selector = (
            By.CSS_SELECTOR,
            "[data-test='inventory-item-name']",
        )
        self.cart_item_count_selector = (
            By.CSS_SELECTOR,
            "[data-test='shopping-cart-badge']",
        )

    def get_price(self):
        return self.get_element_text(self.price_selector)

    def get_product_name(self):
        return self.get_element_text(self.product_name_selector)

    def click_add_to_cart(self):
        self.do_click(self.add_to_cart_button_selector)

    def click_back(self):
        self.do_click(self.back_button_selector)

    def get_number_cart_items(self):
        has_items_in_cart = len(self.get_elements(self.cart_item_count_selector)) > 0
        if has_items_in_cart:
            num_items_in_cart = self.get_element_text(self.cart_item_count_selector)
            return int(num_items_in_cart)
        else:
            return 0
