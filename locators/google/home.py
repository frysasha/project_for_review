from playwright.sync_api import Page

from locators.base_locators import BaseLocators


class GoogleHomeLocators(BaseLocators):
    def __init__(self, page: Page):
        super().__init__(page)
        self.SEARCH_INPUT = self.page.locator('//*[@id="APjFqb"]')