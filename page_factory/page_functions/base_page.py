from actions.page_actions import PageActions
from playwright.async_api import Page
from page_locators.login_page_locators import LoginPageLocators
from utils.common_utils import CommonUtils

class BasePage(PageActions):
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.login_locators = LoginPageLocators()
        self.page.goto(base_url)
    
    # async def goto(self, url: str):
    #     await self.page.goto(url)
    #     return self

    async def enter_username(self, username: str):
        await self.page.fill(LoginPageLocators.USERNAME, username)
        return self

    async def enter_password(self, password: str):
        await self.page.fill(LoginPageLocators.PASSWORD, CommonUtils.decrypt_password(password))
        return self

    async def click_login_button(self):
        await self.page.click(LoginPageLocators.LOGIN_BUTTON)
        return self

    async def login(self, username: str, password: str):
        return await self.enter_username(username).enter_password(password).click_login_button()
    
    async def enter_security_answer(self, locator, question):
        question = self.get_text(self.page, self.login_locators.SECURITY_QUESTION)
        locator = self.login_locators.TEXTBOX_SECURITY_ANSWER
        if question.lower().find('best friend') != -1:
            await self.enter_text(self.page, locator, "Namrata")
        elif question.lower().find('color') != -1:
            await self.enter_text(self.page, locator, "Red")
        elif question.lower().find('sports') != -1:
            await self.enter_text(self.page, locator, "ManUtd")
        return self