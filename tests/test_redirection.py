import allure

from pages.redirect_page import RedirectionPage
from data import RedirectionData

class TestRedirection:
    @allure.description("Проверяем что при переходе на страницу самоката ссылка равна заданной")
    def test_redirection_to_samokat(self, driver):
        redirect_page = RedirectionPage(driver)
        expected_link = RedirectionData.SAMOKAT_PAGE
        actual_link = redirect_page.redirection_to_samokat()
        assert actual_link == expected_link

    @allure.description("Проверяем что при переходе на страницу дзен ссылка равна заданной")
    def test_redirection_to_dzen(self, driver):
        redirect_page = RedirectionPage(driver)
        expected_link = RedirectionData.DZEN_PAGE
        actual_link = redirect_page.redirection_to_dzen()
        assert actual_link == expected_link
