import allure
import logging

logger = logging.getLogger(__name__)


@allure.title("Test Request Demo")
@allure.description("Check that the request demo page is displayed")
def test_request_demo(home_page, request_demo_page):
    assert home_page.is_home_page_displayed()
    home_page.request_demo()
    assert request_demo_page.is_request_demo_page_displayed()


@allure.title("Test About Page")
@allure.description("Check that the about page is displayed")
def test_about_page(home_page, about_page):
    assert home_page.is_home_page_displayed()
    home_page.learn_more()
    assert about_page.is_about_page_displayed()


@allure.title("Test WP API")
@allure.description("Check that the WP API is responding")
def test_wp_api_root(api_context):
    response = api_context.get("/wp-json/")
    assert response.status == 200
    body = response.json()
    assert "name" in body
    assert body["name"] == "Open Innovation AI"
