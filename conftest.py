import os
import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

load_dotenv()

# TODO: move it to .env / GHA env vars as well as params?
HEADLESS = os.getenv("HEADLESS", "true").lower() == "false"
SLOW_MO = int(os.getenv("SLOW_MO", "500"))

# TODO: add a function to clean data (sent emails) after tests?

@pytest.fixture
def base_url(): return os.getenv("BASE_URL")

@pytest.fixture
def email_username(): return os.getenv("EMAIL_USERNAME")

@pytest.fixture
def email_password(): return os.getenv("EMAIL_PASSWORD")

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        yield browser
        browser.close()

@pytest.fixture()
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture()
def page(context):
    page = context.new_page()
    yield page
    page.close()
