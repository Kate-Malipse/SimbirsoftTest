import time
from selenium.webdriver.common.by import By
from src.base.Base import BasePage


class Locators:
    LOCATOR_LOG_IN_BUTTON = (By.CLASS_NAME, "s-btn__filled")
    LOCATOR_LOG_IN_WITH_GOOGLE = (By.CLASS_NAME, "s-btn__google")
    LOCATOR_LOGIN_ELEMENT = (By.ID, "identifierId")
    LOCATOR_NEXT_LOG_BUTTON = (By.ID, "identifierNext")
    LOCATOR_PASS_ELEMENT = (By.NAME, "password")
    LOCATOR_LOGIN_PASSWORD_ERROR_ELEMENT = (By.CLASS_NAME, "o6cuMc")
    LOCATOR_NEXT_PASS_BUTTON = (By.ID, "passwordNext")
    LOCATOR_MAIL_LIST = (
        By.CSS_SELECTOR, 'div.J-J5-Ji.amH.J-JN-I > span:nth-child(1) > span:nth-child(2)')
    LOCATOR_NEW_MAIL_BUTTON = (By.CLASS_NAME, "T-I-KE")
    LOCATOR_NEW_MAIL_TO = (By.NAME, "to")
    LOCATOR_NEW_MAIL_TOPIC = (By.NAME, "subjectbox")
    LOCATOR_NEW_MAIL_TEXT = (By.CLASS_NAME, "tS-tW")
    LOCATOR_NEW_MAIL_SEND_BUTTON = (By.CLASS_NAME, "aoO.v7")
    LOCATOR_SENT_BOX_BUTTON = (By.CSS_SELECTOR, "a[href$='#sent']")
    LOCATOR_LAST_MAIL_ELEMENT = (
        By.CSS_SELECTOR, "div.UI > div:nth-child(2) > div:nth-child(1) > table > tbody > tr:first-child > td.a4W")
    LOCATOR_LAST_MAIL_TOPIC_ELEMENT = (By.CSS_SELECTOR, "h2.hP")


class AuthorizationPageGoogle(BasePage):

    def to_authorization(self):
        self.find_and_click(Locators.LOCATOR_LOG_IN_BUTTON, 2)
        self.find_and_click(Locators.LOCATOR_LOG_IN_WITH_GOOGLE, 1)

    def enter_login(self, login):
        login_element = self.find_element(Locators.LOCATOR_LOGIN_ELEMENT)
        login_element.send_keys(login)
        self.find_and_click(Locators.LOCATOR_NEXT_LOG_BUTTON, 1)

    def enter_password(self, password):
        pass_element = self.find_element(Locators.LOCATOR_PASS_ELEMENT)
        pass_element.send_keys(password)
        self.find_and_click(Locators.LOCATOR_NEXT_PASS_BUTTON, 1)

    def get_enter_error(self):
        return self.find_element(Locators.LOCATOR_LOGIN_PASSWORD_ERROR_ELEMENT, 5).text


class SendNewMailPageGoogle(BasePage):

    def get_inbox_mails_count(self):
        mail_list = self.find_element(Locators.LOCATOR_MAIL_LIST)
        mail_count_total = mail_list.text
        return mail_count_total

    def send_new_mail(self, to, topic, text):
        self.find_and_click(Locators.LOCATOR_NEW_MAIL_BUTTON)

        new_mail_to = self.find_element(Locators.LOCATOR_NEW_MAIL_TO)
        # Ждем анимацию открытия поля "Кому"
        time.sleep(1)
        new_mail_to.send_keys(to)

        new_mail_topic = self.find_element(Locators.LOCATOR_NEW_MAIL_TOPIC)
        new_mail_topic.send_keys(topic)

        new_mail_text = self.find_element(Locators.LOCATOR_NEW_MAIL_TEXT)
        new_mail_text.send_keys(text)

        self.find_and_click(Locators.LOCATOR_NEW_MAIL_SEND_BUTTON)

    def get_last_sent_mail_topic(self):
        self.find_and_click(Locators.LOCATOR_SENT_BOX_BUTTON)
        self.find_and_click(Locators.LOCATOR_LAST_MAIL_ELEMENT)
        topic = self.find_element(Locators.LOCATOR_LAST_MAIL_TOPIC_ELEMENT)
        return topic.text
