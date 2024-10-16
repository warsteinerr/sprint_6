import allure
import pytest
from data import TestData
from pages.main_page import MainPage

@pytest.mark.parametrize('num, result', TestData.TEST_DATA)

class TestMainPage:

    @allure.description('На главной странице получаем ответ на каждый вопрос и сравниваем его с ожидаемым')
    def test_right_answers(self, driver, num, result):
        main_page = MainPage(driver)
        assert main_page.get_answer_text(num) == result

