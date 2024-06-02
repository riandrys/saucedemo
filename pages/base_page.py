from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._driver_wait = WebDriverWait(driver, 30)

    def do_click(self, by_locator: tuple[str, str]):
        self.get_element(by_locator).click()

    def get_element(self, by_locator: tuple[str, str]):
        return self._driver.find_element(*by_locator)

    def do_send_keys(self, by_locator: tuple[str, str], text: str):
        element = self.get_element(by_locator)
        element.clear()
        element.send_keys(text)

    def press_enter(self, by_locator: tuple[str, str]):
        element = self.get_element(by_locator)
        element.send_keys(Keys.ENTER)

    def get_element_text(self, by_locator: tuple[str, str]):
        element = self.get_element(by_locator)
        return element.text

    def is_visible(self, by_locator: tuple[str, str]):
        element = self.get_element(by_locator)
        return bool(element)

    def open(self, url):
        self._driver.get(url)

    def get_title(self):
        return self._driver.title

    def get_url(self):
        return self._driver.current_url

    def maximize(self):
        self._driver.maximize_window()
