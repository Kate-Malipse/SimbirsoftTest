from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Base import BasePage 
import time

class Locators:
    #Yandex
    LOCATOR_ENTER_BUTTON_Y = (By.CLASS_NAME, "HeadBanner-Button-Enter")
    LOCATOR_LOGIN_ELEMENT_Y = (By.NAME, "login")
    LOCATOR_PASS_ELEMENT_Y = (By.NAME, "passwd")
    LOCATOR_NEXT_BUTTON_Y = (By.CLASS_NAME, "button2_type_submit")
    LOCATOR_MAIL_LIST_Y = (By.CLASS_NAME, "mail-NestedList-Item-Info-Extras")
    LOCATOR_NEW_MAIL_BUTTON_Y = (By.CLASS_NAME, "mail-ComposeButton")
    LOCATOR_NEW_MAIL_TO_Y = (By.CLASS_NAME, "composeYabbles")
    LOCATOR_NEW_MAIL_TOPIC_Y = (By.NAME, "subject")
    LOCATOR_NEW_MAIL_TEXT_Y = (By.CLASS_NAME, "cke_htmlplaceholder")
    LOCATOR_NEW_MAIL_SEND_BUTTON_Y = (By.CLASS_NAME, "ComposeControlPanelButton-Button_action")

    #Google
    LOCATOR_LOG_IN_BUTTON_G = (By.CLASS_NAME,"s-btn__filled")
    LOCATOR_LOG_IN_WITH_GOOGLE = (By.CLASS_NAME, "s-btn__google")
    LOCATOR_LOGIN_ELEMENT_G = (By.ID, "identifierId")
    LOCATOR_NEXT_LOG_BUTTON_G = (By.ID, "identifierNext")
    LOCATOR_PASS_ELEMENT_G = (By.NAME, "password")
    LOCATOR_NEXT_PASS_BUTTON_G = (By.ID, "passwordNext")
    LOCATOR_MAIL_LIST_G = (By.CSS_SELECTOR, 'div.J-J5-Ji.amH.J-JN-I > span:nth-child(1) > span:nth-child(2)')
    LOCATOR_NEW_MAIL_BUTTON_G = (By.CLASS_NAME, "T-I-KE")
    LOCATOR_NEW_MAIL_TO_G = (By.NAME, "to")
    LOCATOR_NEW_MAIL_TOPIC_G = (By.NAME, "subjectbox")
    LOCATOR_NEW_MAIL_TEXT_G = (By.CLASS_NAME, "tS-tW")
    LOCATOR_NEW_MAIL_SEND_BUTTON_G = (By.CLASS_NAME, "aoO.v7")

#Classes for Yandex
class AuthorizationPageYandex (BasePage):
    
    def to_authorization(self):
        self.find_and_click(Locators.LOCATOR_ENTER_BUTTON_Y)

    def enter_logo_pass(self, login, passw):
        login_element = self.find_element(Locators.LOCATOR_LOGIN_ELEMENT_Y)
        login_element.send_keys(login)

        self.find_and_click(Locators.LOCATOR_NEXT_BUTTON_Y)

        pass_element = self.find_element(Locators.LOCATOR_PASS_ELEMENT_Y)
        pass_element.send_keys(passw)

        self.find_and_click(Locators.LOCATOR_NEXT_BUTTON_Y)
        
        return login_element, pass_element

class SendNewMailPageYandex (BasePage):

    def mail_count (self):
        mail_list = self.find_element(Locators.LOCATOR_MAIL_LIST_Y)
        mail_count_total = mail_list.text[3:]
        return mail_count_total

    def send_new_mail(self, to, topic, text):
        self.find_and_click(Locators.LOCATOR_NEW_MAIL_BUTTON_Y)

        new_mail_to = self.find_element(Locators.LOCATOR_NEW_MAIL_TO_Y)
        new_mail_to.send_keys(to)

        new_mail_topic = self.find_element(Locators.LOCATOR_NEW_MAIL_TOPIC_Y)
        new_mail_topic.send_keys(topic)

        new_mail_text = self.find_element(Locators.LOCATOR_NEW_MAIL_TEXT_Y)
        new_mail_text.send_keys(text)

        self.find_and_click(Locators.LOCATOR_NEW_MAIL_SEND_BUTTON_Y)

        #return new_mail_send_button

#Classes for Google
class AuthorizationPageGoogle(BasePage):

    def to_authorization(self):
        self.find_and_click(Locators.LOCATOR_LOG_IN_BUTTON_G)
        self.find_and_click(Locators.LOCATOR_LOG_IN_WITH_GOOGLE)

    def enter_logo_pass(self, login, passw):
        login_element = self.find_element(Locators.LOCATOR_LOGIN_ELEMENT_G)
        login_element.send_keys(login)

        self.find_and_click(Locators.LOCATOR_NEXT_LOG_BUTTON_G)

        pass_element = self.find_element(Locators.LOCATOR_PASS_ELEMENT_G)
        pass_element.send_keys(passw)

        self.find_and_click(Locators.LOCATOR_NEXT_PASS_BUTTON_G)

        return login_element, pass_element

class SendNewMailPageGoogle(BasePage):

    def mail_count(self):
        mail_list = self.find_element(Locators.LOCATOR_MAIL_LIST_G)
        mail_count_total = mail_list.text
        return mail_count_total

    def send_new_mail(self, to, topic, text):
        self.find_and_click(Locators.LOCATOR_NEW_MAIL_BUTTON_G)

        new_mail_to = self.find_element(Locators.LOCATOR_NEW_MAIL_TO_G)
        #for open "To" field
        time.sleep(1)
        new_mail_to.send_keys(to)

        new_mail_topic = self.find_element(Locators.LOCATOR_NEW_MAIL_TOPIC_G)
        new_mail_topic.send_keys(topic)

        new_mail_text = self.find_element(Locators.LOCATOR_NEW_MAIL_TEXT_G)
        new_mail_text.send_keys(text)

        self.find_and_click(Locators.LOCATOR_NEW_MAIL_SEND_BUTTON_G)

        #return new_mail_send_button



