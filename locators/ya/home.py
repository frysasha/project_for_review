from playwright.sync_api import Page

from locators.base_locators import BaseLocators


class YaHomeLocators(BaseLocators):
    def __init__(self, page: Page):
        super().__init__(page)
        self.SEARCH_INPUT = self.page.locator('//html/body/main/div[2]/form/div[4]/div[2]/div[2]/div[2]/div/input')
        self.WEATHER = self.page.locator('[data-statlog*=weather]')
        self.SEARCH_RESULT = self.page.locator("[id*=suggest-list]")