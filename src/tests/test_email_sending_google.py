import pytest
from selenium.webdriver.support.wait import TimeoutException
from src.pages.GooglePages import AuthorizationPageGoogle
from src.pages.GooglePages import SendNewMailPageGoogle

def test_send_new_mail_google(driver):

    # Authorization using stackoverflow
    authorization_page = AuthorizationPageGoogle(driver)
    authorization_page.go_to_site("https://stackoverflow.com/")
    authorization_page.to_authorization()
    # Enter login/password
    authorization_page.enter_logo_pass(
        "login", "password")

    # Send new mail
    send_new_mail_page = SendNewMailPageGoogle(driver)
    send_new_mail_page.go_to_site("https://gmail.com/")
    mail_count = send_new_mail_page.mail_count()
    # Enter email(to), subject and message
    send_new_mail_page.send_new_mail(
        "example@mail.ru", "Тестовое задание. Малеванная", mail_count)
    
