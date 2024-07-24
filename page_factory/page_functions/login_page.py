from actions.page_actions import PageActions
from playwright.async_api import Page
from page_factory.page_locators.login_page_locators import LoginPageLocators
from utils.common_utils import CommonUtils
# from home_page import HomePage

class LoginPage(PageActions):
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.locators = LoginPageLocators()
        self.page.goto(base_url)
        self.utils = CommonUtils()
    
    # def goto(self, url: str):
    #     self.page.goto(url)
    #     return self

    def enter_username(self, username: str):
        self.page.fill(self.locators.USERNAME, username)
        return self

    def enter_password(self, password: str):
        final_pwd = self.utils.decrypt_password(password)
        self.page.fill(self.locators.PASSWORD, final_pwd)
        return self

    def click_login_button(self):
        self.page.click(self.locators.LOGIN_BUTTON)
        return self

    def login(self, username: str, password: str):
        return self.enter_username(username).enter_password(password).click_login_button().enter_security_answer()
    
    def enter_security_answer(self):
        question = self.page.text_content(self.locators.SECURITY_QUESTION)
        locator = self.locators.TEXTBOX_SECURITY_ANSWER
        if question.lower().find('best friend') != -1:
            self.enter_text(self.page, locator, "Namrata")
        elif question.lower().find('color') != -1:
            self.enter_text(self.page, locator, "Red")
        elif question.lower().find('sports') != -1:
            self.enter_text(self.page, locator, "ManUtd")
        return self