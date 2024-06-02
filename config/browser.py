from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def get_browser(browser_name, headless, mobile):
    if browser_name.lower() == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        if mobile:
            mobile_emulation = {"deviceName": mobile}
            options.add_experimental_option("mobileEmulation", mobile_emulation)
        web_driver = webdriver.Chrome(options=options)
    elif browser_name.lower() == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        web_driver = webdriver.Firefox(options=options)
    elif browser_name.lower() == "safari":
        web_driver = webdriver.Safari(options=webdriver.SafariOptions())

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    web_driver.maximize_window()
    return web_driver
