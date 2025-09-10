from playwright.sync_api import Page

from locators.ya.home import YaHomeLocators
from pages.base_page import BasePage


class YaHomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.locators = YaHomeLocators(page)