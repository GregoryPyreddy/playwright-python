from page_factory.page_functions.login_page import LoginPage
from utils.contants import Constants
class TestTC10001:
    def test_TC10001(self, browser_page, base_url):
        login_page = LoginPage(page=browser_page, base_url=base_url)
        login_page.login(Constants.USERNAME, Constants.HASHED_PASSWORD)

