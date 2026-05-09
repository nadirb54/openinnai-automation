import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class RequestDemoPage(BasePage):
    def __init__(self, page: Page):
        self.page = page

    def is_request_demo_page_displayed(self) -> bool:
        try:
            expect(self.page).to_have_url(re.compile(r"/request-demo/$"))
            expect(self.page).to_have_title("Request Demo - Open Innovation AI")
            return True
        except AssertionError:
            return False
