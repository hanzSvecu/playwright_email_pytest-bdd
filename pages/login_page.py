from pathlib import Path

from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email = page.get_by_test_id('tfi:mailAddress_label')
        self.password = page.get_by_test_id('tfi:password_label')
        self.login_btn = page.get_by_test_id('btn:login_action')

    def open(self, base_url: str):
        self.page.goto(base_url, wait_until="domcontentloaded")
        # to check problematic part
        try:
            self.is_loaded()
        except Exception:
            Path("artifacts").mkdir(exist_ok=True)
            print(f"Current URL: {self.page.url}")
            self.page.screenshot(
                path="artifacts/login-page-failed.png",
                full_page=True
            )
            with open("artifacts/login-page-failed.html", "w", encoding="utf-8") as f:
                f.write(self.page.content())
            raise

    def is_loaded(self):
        expect(self.login_btn).to_be_attached(timeout=10000)
        expect(self.login_btn).to_be_visible(timeout=10000)

    def fill_email(self, email: str):
        self.email.click()
        self.email.fill(email)

    def fill_password(self, password: str):
        self.password.click()
        self.password.fill(password)

    def click_login(self):
        self.login_btn.click()

    def perform_login(self, email: str, password: str):
        self.fill_email(email)
        self.fill_password(password)
        self.click_login()
