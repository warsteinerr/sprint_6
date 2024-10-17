from selenium.webdriver.common.by import By


class OrderPageLocators:
    COOKIES_BTN = By.ID, 'rcc-confirm-button'
    NAME = By.XPATH, '//input[@placeholder="* Имя"]'  #Поле имя
    SURNAME = By.XPATH, '//input[@placeholder="* Фамилия"]'  # Поле Фамилия
    ADDRESS = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'  #ПолеАдрес
    METRO = By.CLASS_NAME, 'select-search'  # Поле выбора метро
    PHONE = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'  # Поле для номера телефона
    GO_ON_BUTTON = By.XPATH, '//button[text()="Далее"]'  # кнопка далее
    DELIVERY_DATE = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'  #Поле когда привезти самокат.
    RENTAL_PERIOD = By.XPATH, '//div[text()="* Срок аренды"]'  #Поле срок аренды
    COMMENT = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'  # Комментарий для курьера
    BLACK = By.ID, 'black'  # Чёрный жемчуг
    GREY = By.ID, 'grey'  # Серая безысходность
    ORDER_BUTTON = By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]' # Кнопка Заказать
    WANT_ORDER_TEXT = By.XPATH, '//*[text()="Хотите оформить заказ?"]'  # Текст Хотите оформить заказ?
    ORDER_PLACED = By.XPATH, '//*[text()="Заказ оформлен"]'  # Текст заказ оформлен
    SQUARE = By.XPATH, '//ul/li[3]'  # Преображенская площадь
    DELIVERY_DATE_1 = By.XPATH, '//div[@class ="react-datepicker__month"]/div[1]/div[1]'  # Первая цифра в открывшемся календаре
    ONE_DAY = By.XPATH, '//div[text()="сутки"]'  # Значение сутки.
    CHERKIZOVO = By.XPATH, '//ul/li[2]'  # Метро Черкизовская
    DELIVERY_DATE_2 = By.XPATH, '//div[@class ="react-datepicker__month"]/div[1]/div[2]'  # Вторая цифра в открывшемся календаре
    TWO_DAYS = By.XPATH, '//div[text()="двое суток"]'  #Значеник периода двое суток
    ABOUT_RENT = By.XPATH, '//*[text()="Про аренду"] '  # Заголовок Про аренду
    YES_BUTTON = By.XPATH, '//*[text()="Да"]'  # Кнопка Да в подтверждении заказа



