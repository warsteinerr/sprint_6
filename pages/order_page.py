import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step("Заполняем первый блок страницы заказа и переходим ко второму блоку")
    def fill_first_order_block(self,order_button, name, surname, address, metro_station, phone_number):
        self.get_link('https://qa-scooter.praktikum-services.ru')
        self.click_on_element(OrderPageLocators.COOKIES_BTN)
        self.scroll_to_element(order_button)
        self.click_on_element(order_button)
        self.send_keys_to_element(OrderPageLocators.NAME, name)
        self.send_keys_to_element(OrderPageLocators.SURNAME, surname)
        self.send_keys_to_element(OrderPageLocators.ADDRESS, address)
        self.click_on_element(OrderPageLocators.METRO)
        self.click_on_element(metro_station)
        self.send_keys_to_element(OrderPageLocators.PHONE, phone_number)
        self.click_on_element(OrderPageLocators.GO_ON_BUTTON)

    @allure.step("Заполняем второй блок страницы заказа и подтверждаем его")
    def fill_second_order_block(self, date, period, colour, comment):
        self.click_on_element(OrderPageLocators.DELIVERY_DATE)
        self.click_on_element(date)
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_on_element(period)
        self.click_on_element(colour)
        self.send_keys_to_element(OrderPageLocators.COMMENT, comment)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.YES_BUTTON)











