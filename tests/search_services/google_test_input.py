from time import sleep

import pytest
from playwright.sync_api import Page, expect

from pages.google.home import GoogleHomePage


class TestGoogle:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = GoogleHomePage(page)

    def test_google(self):
        self.page.open("https://www.google.com/")
        self.page.expect_title("Google")
        self.page.locators.SEARCH_INPUT.fill("python")
        sleep(2)
        expect(self.page.locators.SEARCH_INPUT).to_contain_text("python")