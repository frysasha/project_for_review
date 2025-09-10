from playwright.sync_api import Page

from locators.google.home import GoogleHomeLocators
from pages.base_page import BasePage


class GoogleHomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = GoogleHomeLocators(page)