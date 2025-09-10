from time import sleep

import pytest
from playwright.sync_api import Page, expect

from pages.exceptions import WeatherNotFound
from pages.ya.home import YaHomePage


class TestYaRu:

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = YaHomePage(page)

    def test_ya_ru(self):
        self.page.open("https://ya.ru")
        self.page.expect_title("Яндекс — быстрый поиск в интернете")
        self.page.locators.SEARCH_INPUT.fill("python")
        self.page.expect_text("python")

    def test_ya_ru_search(self):
        self.page.open("https://ya.ru")
        self.page.expect_title("Яндекс — быстрый поиск в интернете")
        self.page.locators.SEARCH_INPUT.fill("python")
        sleep(2) # ожидаем когда появится результат поиска
        expect(self.page.locators.SEARCH_RESULT).to_contain_text("python")

    def test_ya_weather(self):
        self.page.open("https://ya.ru")
        self.page.expect_title("Яндекс — быстрый поиск в интернете")
        try:
            self.page.locators.WEATHER.is_visible()
        except Exception:
            raise WeatherNotFound("Weather not found")