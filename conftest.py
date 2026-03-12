import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose language (for example "ru")',
    )


@pytest.fixture
def browser(request: pytest.FixtureRequest):
    language = request.config.getoption('language')

    options = Options()
    options.add_experimental_option(
        'prefs',
        {
            'intl.accept_languages': language
        }
    )

    web_driver: WebDriver = webdriver.Chrome(options=options)
    yield web_driver
    web_driver.quit()
