import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class AboutPage(BasePage):
    def __init__(self, page: Page):
        self.page = page

    def is_about_page_displayed(self) -> bool:
        try:
            expect(self.page).to_have_url(re.compile(r"/about/$"))
            expect(self.page).to_have_title("About Open Innovation AI")
            return True
        except AssertionError:
            return False
