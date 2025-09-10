from typing import Literal

import allure
from playwright.sync_api import Page, expect

from locators.base_locators import BaseLocators


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_locators = BaseLocators(page)

    @allure.step("Открыть страницу {url}")
    def open(self, url: str) -> None:
        self.page.goto(url)

    @allure.step("Страница содержит title '{title}'")
    def expect_title(self, title: str) -> None:
        expect(self.page).to_have_title(title)

    @allure.step("Страница содержит text '{text}'")
    def expect_text(self, text: str) -> None:
        for el in self.page.get_by_text(text).all():
            expect(el).to_be_visible()

    @allure.step("Страница содержит URL '{url}'")
    def expect_url(self, url: str) -> None:
        expect(self.page).to_have_url(url)

    @allure.step("Обновить страницу")
    def refresh_page(self, wait: Literal["commit", "domcontentloaded", "load", "networkidle"]) -> None:
        self.page.reload(wait_until=wait)

    @allure.step("Открыть новую вкладку")
    def open_new_tab(self) -> Page:
        new_page = self.page.context.new_page()
        return new_page

    @allure.step("Нажать на клавишу '{button}'")
    def press_keyboard_button(self, button: str) -> None:
        self.page.keyboard.press(button)

    @allure.step("Закрыть вкладку по индексу '{index}'")
    def close_page_by_index(self, index: int) -> None:
        pages = self.page.context.pages
        pages[index].close()
