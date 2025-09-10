import pytest
from playwright.sync_api import BrowserContext, Page, Browser, Playwright


@pytest.fixture(scope="session")
def get_browser(request: pytest.FixtureRequest, playwright: Playwright) -> Browser:
    browser = playwright.chromium.launch(channel="chrome", args=["--start-maximized"])
    return browser


@pytest.fixture(scope="session")
def context(request: pytest.FixtureRequest, get_browser: Browser) -> BrowserContext:
    browser = get_browser
    context = browser.new_context()
    yield context

    context.close()
    browser.close()


@pytest.fixture(scope="session")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page
    page.close()
