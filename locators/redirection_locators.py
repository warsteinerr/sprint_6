from selenium.webdriver.common.by import By

class RedirectionLocators:
    COOKIES_BTN = By.ID, 'rcc-confirm-button'
    YANDEX_LOGO = By.XPATH, '//img[@src = "/assets/ya.svg"]'  # Надпись Яндекс в шапке
    SANOKAT_LOGO = By.XPATH, '//img[@src = "/assets/scooter.svg"]'  # Надпись самокат в шапке
