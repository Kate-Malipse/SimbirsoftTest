import pytest
import time
from datetime import datetime
from selenium.webdriver.support.wait import TimeoutException
from src.pages.GooglePages import AuthorizationPageGoogle
from src.pages.GooglePages import SendNewMailPageGoogle

# Вспомогательные функции


def to_authorization_page(driver):
    authorization_page = AuthorizationPageGoogle(driver)
    # Авторизация через stackoverflow
    authorization_page.go_to_site("https://stackoverflow.com/")
    authorization_page.to_authorization()

    return authorization_page

# Тесты
# 1 Тест ввода верного логина


def test_login_positve(driver):
    authorization_page = to_authorization_page(driver)
    authorization_page.enter_login("login")
    with pytest.raises(TimeoutException):
        authorization_page.get_enter_error()

# 2 Тест ввода неверного логина


def test_login_negative(driver):
    #pytest.skip("Пропуск теста")
    authorization_page = to_authorization_page(driver)
    authorization_page.enter_login("wrong_login")

    error_message = authorization_page.get_enter_error()
    assert len(error_message.strip()) > 0

# 3 Тест ввода верного пароля


def test_password_positve(driver):
    authorization_page = to_authorization_page(driver)
    authorization_page.enter_login("login")
    authorization_page.enter_password("password")
    with pytest.raises(TimeoutException):
        authorization_page.get_enter_error()

# 4 Тест ввода неверного пароля


def test_password_negative(driver):
    #pytest.skip("Пропуск теста")
    authorization_page = to_authorization_page(driver)
    authorization_page.enter_login("login")
    authorization_page.enter_password("qwerty1234")

    error_message = authorization_page.get_enter_error()
    assert len(error_message.strip()) > 0

# 5 Тест отправки нового письма (позитивный сценарий)


def test_send_new_mail(driver):
    authorization_page = to_authorization_page(driver)
    authorization_page.enter_login("login")
    authorization_page.enter_password("password")
    send_new_mail_page = SendNewMailPageGoogle(driver)
    # Переходим на почту Google
    send_new_mail_page.go_to_site("https://gmail.com/")
    mails_count = send_new_mail_page.get_inbox_mails_count()

    # Проверка значения переданного из элемента о количестве писем
    assert mails_count.isdigit() == True, "Найденное значение не является кол-вом писем"

    current_datetime = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    topic = f"{current_datetime} Тестовое задание. Малеванная"

    send_new_mail_page.send_new_mail("example@gmail.com", topic, mails_count)

    # Ожидаем когда отправиться письмо и проверяем его в отправленных
    time.sleep(10)
    last_topic = send_new_mail_page.get_last_sent_mail_topic()
    assert last_topic == topic
