import pytest
import os
import allure
import time
import shutil
from dotenv import load_dotenv

load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--resolution",
        action="store",
        default="desktop",
        choices=["desktop", "tablet", "phone"],
        help="Screen resolution to simulate: desktop, tablet, or phone",
    )


# ===== Fixtures =====


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")


@pytest.fixture(scope="function")
def context(browser, pytestconfig):
    resolution_map = {
        "desktop": {"width": 1920, "height": 1080},
        "tablet": {"width": 1024, "height": 768},
        "phone": {"width": 430, "height": 932},
    }
    resolution = pytestconfig.getoption("resolution")
    viewport = resolution_map.get(resolution, resolution_map["desktop"])

    context = browser.new_context(viewport=viewport)
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context, base_url):
    page = context.new_page()
    page.goto(base_url, wait_until="domcontentloaded")
    yield page
    page.close()


@pytest.fixture(scope="function")
def api_context(playwright, base_url):
    context = playwright.request.new_context(base_url=base_url)
    yield context
    context.dispose()


# ==== Reporting ====


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        timestamp = int(time.time() * 1000)
        page = item.funcargs.get("page")

        screenshot_dir = os.path.join(os.getcwd(), "reports/screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)

        if page:
            try:
                screenshot_path = os.path.join(
                    screenshot_dir, f"{item.name}_page1_{timestamp}.png"
                )
                context = page.context
                pages = context.pages
                target = page if len(pages) == 1 else pages[-1]
                target.screenshot(path=screenshot_path)
                allure.attach(
                    open(screenshot_path, "rb").read(),
                    name="Page 1 Screenshot",
                    attachment_type=allure.attachment_type.PNG,
                )
            except Exception as e:
                print(f"[Screenshot] Failed for page1: {e}")


@pytest.hookimpl()
def pytest_sessionstart(session):
    # With xdist, only run on the controller process, not on workers
    if getattr(session.config, "workerinput", None) is not None:
        return

    reports_dir = "reports"
    if os.path.exists(reports_dir):
        shutil.rmtree(reports_dir)
    os.makedirs(reports_dir)
    allure_results_dir = os.path.join(reports_dir, "allure-results")
    os.makedirs(allure_results_dir, exist_ok=True)
    browser_list = session.config.getoption("browser")
    browser = browser_list[0].capitalize() if browser_list else "Chromium"
    resolution = session.config.getoption("resolution").capitalize()
    env_props = f"Browser={browser}\nResolution={resolution}\n"
    with open(os.path.join(allure_results_dir, "environment.properties"), "w") as f:
        f.write(env_props)


# ===== Instantiate application pages =====


@pytest.fixture(scope="function")
def about_page(page):
    from pages.about_page import AboutPage

    yield AboutPage(page)


@pytest.fixture(scope="function")
def home_page(page):
    from pages.home_page import HomePage

    yield HomePage(page)


@pytest.fixture(scope="function")
def request_demo_page(page):
    from pages.request_demo_page import RequestDemoPage

    yield RequestDemoPage(page)
