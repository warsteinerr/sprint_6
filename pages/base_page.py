from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def explicit_wait(self, locator):
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )
        return element


    def click_on_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def send_keys_to_element(self, locator, key):
        self.explicit_wait(locator).send_keys(key)

    def get_text_from_element(self, locator):
        return self.explicit_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.explicit_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def format_locators(self, locator_template, num):
        method, locator = locator_template
        locator = locator.format(num)
        return method, locator

    def check_element_is_displayed(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return element.is_displayed()

    def get_link(self, link):
        self.driver.get(link)

    def url_to_be_visible(self, link):
        WebDriverWait(self.driver, 10).until(
            EC.url_contains(link)
        )

    def wait_for_new_tab_and_switch(self):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
