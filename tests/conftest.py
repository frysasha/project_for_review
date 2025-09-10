import pytest
from playwright.sync_api import BrowserContext, Page, Browser, Playwright


@pytest.fixture()
def get_browser(request: pytest.FixtureRequest, playwright: Playwright) -> Browser:
    """Фикстура отвечающая за запуск браузера, в зависимости от режима запуска (локальный или удаленный)
    и удаленного драйвера (если выбран удаленный режим)"""

    browser = playwright.chromium.launch(
        channel="chrome", headless=request.config.getoption("--headless"), args=["--start-maximized"]
    )
    return browser


@pytest.fixture(scope="function")
def context(request: pytest.FixtureRequest, get_browser: Browser, test_name: str) -> BrowserContext:
    browser = get_browser
    context = browser.new_context(
        no_viewport=True
    )
    yield context

    context.close()
    browser.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page
    page.close()