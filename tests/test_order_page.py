import allure
import pytest
from data import OrderData
from pages.order_page import OrderPage

@pytest.mark.parametrize('order_button, name, surname, address, metro_station, phone_number, date, period, colour, comment, expected_element',
                         OrderData.ORDER_DATA)


class TestOrderPage:
    @allure.description("Тест заполняет полностью форму заказа, подтверждает его и проверяет что 'Заказ оформлен' отображается ")
    def test_check_order(self, driver, order_button, name, surname, address, metro_station, phone_number, date, period, colour, comment, expected_element):
        order_page = OrderPage(driver)
        order_page.fill_first_order_block(order_button, name, surname, address, metro_station, phone_number)
        order_page.fill_second_order_block(date, period, colour, comment)
        assert order_page.check_element_is_displayed(expected_element)


