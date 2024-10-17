import allure

from pages.base_page import BasePage
from locators.redirection_locators import RedirectionLocators
from data import RedirectionData
class RedirectionPage(BasePage):
    @allure.step("Кликаем на лого самоката и ждем пока url будет равен заданному и возвращаем его")
    def redirection_to_samokat(self):
        self.get_link('https://qa-scooter.praktikum-services.ru/order')
        self.click_on_element(RedirectionLocators.COOKIES_BTN)
        self.click_on_element(RedirectionLocators.SANOKAT_LOGO)
        self.url_to_be_visible(RedirectionData.SAMOKAT_PAGE)
        return self.driver.current_url

    @allure.step("Кликаем на лого яндекса, переключаемся на новое окно и ждем пока url будет равен заданному и возвращаем его")
    def redirection_to_dzen(self):
        self.get_link('https://qa-scooter.praktikum-services.ru/order')
        self.click_on_element(RedirectionLocators.COOKIES_BTN)
        self.click_on_element(RedirectionLocators.YANDEX_LOGO)
        self.wait_for_new_tab_and_switch()
        self.url_to_be_visible(RedirectionData.DZEN_PAGE)
        return self.driver.current_url





