from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.request_demo_button = page.get_by_text("Request a demo").nth(1)
        self.learn_more_button = page.get_by_text("Learn more")

    def is_home_page_displayed(self) -> bool:
        try:
            expect(self.page).to_have_title(
                "Open Innovation AI – Enterprise AI Infrastructure Simplified"
            )
            return True
        except AssertionError:
            return False

    def request_demo(self) -> None:
        self.request_demo_button.click()

    def learn_more(self) -> None:
        self.learn_more_button.click()
