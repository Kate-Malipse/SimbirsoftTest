from selenium.webdriver.common.by import By
from src.base.Base import BasePage


class Locators:
    LOCATOR_ENTER_BUTTON = (By.CLASS_NAME, "HeadBanner-Button-Enter")
    LOCATOR_LOGIN_ELEMENT = (By.NAME, "login")
    LOCATOR_PASS_ELEMENT = (By.NAME, "passwd")
    LOCATOR_LOGIN_PASSWORD_ERROR_ELEMENT = (
        By.CLASS_NAME, "passp-form-field__error")
    LOCATOR_NEXT_BUTTON = (By.CLASS_NAME, "button2_type_submit")
    LOCATOR_MAIL_LIST = (By.CSS_SELECTOR, "a[href='#inbox'] > div > span")
    LOCATOR_NEW_MAIL_BUTTON = (By.CLASS_NAME, "mail-ComposeButton")
    LOCATOR_NEW_MAIL_TO = (By.CLASS_NAME, "composeYabbles")
    LOCATOR_NEW_MAIL_TOPIC = (By.NAME, "subject")
    LOCATOR_NEW_MAIL_TEXT = (By.CLASS_NAME, "cke_htmlplaceholder")
    LOCATOR_NEW_MAIL_SEND_BUTTON = (
        By.CLASS_NAME, "ComposeControlPanelButton-Button_action")
    LOCATOR_SENT_BOX_BUTTON = (By.CSS_SELECTOR, "a[href='#sent']")
    LOCATOR_LAST_MAIL_ELEMENT = (
        By.CSS_SELECTOR, "div.mail-MessagesList > div:first-child")
    LOCATOR_LAST_MAIL_TOPIC_ELEMENT = (
        By.CLASS_NAME, "mail-Message-Toolbar-Subject")


class AuthorizationPageYandex (BasePage):
    def to_authorization(self):
        self.find_and_click(Locators.LOCATOR_ENTER_BUTTON)

    def enter_login(self, login):
        login_element = self.find_element(Locators.LOCATOR_LOGIN_ELEMENT)
        login_element.send_keys(login)
        self.find_and_click(Locators.LOCATOR_NEXT_BUTTON)

    def enter_password(self, password):
        pass_element = self.find_element(Locators.LOCATOR_PASS_ELEMENT)
        pass_element.send_keys(password)
        self.find_and_click(Locators.LOCATOR_NEXT_BUTTON)

    def get_enter_error(self):
        return self.find_element(Locators.LOCATOR_LOGIN_PASSWORD_ERROR_ELEMENT, 5).text


class SendNewMailPageYandex (BasePage):
    def get_inbox_mails_count_string(self):
        mail_list_string = self.find_element(Locators.LOCATOR_MAIL_LIST)
        # Условие для Chrome т.к. не передается текст элемента
        if len(mail_list_string.text) > 0:
            return mail_list_string.text
        else:
            return mail_list_string.get_attribute("innerHTML")

    def send_new_mail(self, to, topic, text):
        self.find_and_click(Locators.LOCATOR_NEW_MAIL_BUTTON)

        new_mail_to = self.find_element(Locators.LOCATOR_NEW_MAIL_TO)
        new_mail_to.send_keys(to)

        new_mail_topic = self.find_element(Locators.LOCATOR_NEW_MAIL_TOPIC)
        new_mail_topic.send_keys(topic)

        new_mail_text = self.find_element(Locators.LOCATOR_NEW_MAIL_TEXT)
        new_mail_text.send_keys(text)

        self.find_and_click(Locators.LOCATOR_NEW_MAIL_SEND_BUTTON)

    def get_last_sent_mail_topic(self):
        self.find_and_click(Locators.LOCATOR_SENT_BOX_BUTTON)
        # Игнорирование баннеров
        self.find_and_click(Locators.LOCATOR_SENT_BOX_BUTTON)
        self.find_and_click(Locators.LOCATOR_LAST_MAIL_ELEMENT)
        topic = self.find_element(Locators.LOCATOR_LAST_MAIL_TOPIC_ELEMENT)
        return topic.text
