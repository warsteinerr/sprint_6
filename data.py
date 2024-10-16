from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators

class OrderData:
    ORDER_DATA = [(MainPageLocators.UP_ORDER_BUTTON, 'Иван', 'Иванов', 'улица Пушкина', OrderPageLocators.SQUARE, '89277090909',
                           OrderPageLocators.DELIVERY_DATE_1, OrderPageLocators.ONE_DAY, OrderPageLocators.BLACK, 'камент', OrderPageLocators.ORDER_PLACED),
                  (MainPageLocators.DOWN_ORDER_BUTTON, 'Петров', 'Петр', 'улица Есенина', OrderPageLocators.CHERKIZOVO, '89272070707',
                           OrderPageLocators.DELIVERY_DATE_2, OrderPageLocators.TWO_DAYS, OrderPageLocators.GREY, 'камент2', OrderPageLocators.ORDER_PLACED)]



class TestData:
    TEST_DATA =[(0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
                (1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
                (2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
                (3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
                (4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
                (5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
                (6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
                (7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
                ]


class RedirectionData:
    SAMOKAT_PAGE = 'https://qa-scooter.praktikum-services.ru/'
    DZEN_PAGE = 'https://dzen.ru/?yredirect=true'
