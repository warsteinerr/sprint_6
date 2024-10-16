import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Получаем текст ответа на вопрос')
    def get_answer_text(self, num):
        self.get_link('https://qa-scooter.praktikum-services.ru/')
        self.click_on_element(MainPageLocators.COOKIES_BTN)
        last_element = self.format_locators(MainPageLocators.QUESTION, num)
        self.scroll_to_element(last_element)
        question_locator = self.format_locators(MainPageLocators.QUESTION, num)
        answer_locator = self.format_locators(MainPageLocators.ANSWER, num)
        self.click_on_element(question_locator)
        return self.get_text_from_element(answer_locator)

