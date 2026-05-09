import allure


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
