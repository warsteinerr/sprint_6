from selenium.webdriver.common.by import By


class MainPageLocators:
    ACTUAL_QUESTIONS = By.XPATH, '//div[text()="Вопросы о важном"]'  # Заголовок раздела вопросы о важном
    COOKIES_BTN = By.ID, 'rcc-confirm-button'  # Кнопка принятия кукиз
    QUESTION = By.XPATH, '//*[@id="accordion__heading-{}"]'
    ANSWER= By.XPATH, '//*[@id="accordion__panel-{}"]/p'
    UP_ORDER_BUTTON = By.XPATH, '//button[text()="Статус заказа"]/parent::div/button[text()="Заказать"]'  # Верхняя кнопка заказать
    DOWN_ORDER_BUTTON = By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button'  #Нижняя кнопка заказать

