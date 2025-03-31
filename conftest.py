import re
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@allure.title("Get chrome options")
@pytest.fixture(name="get_chrome_options", scope="class")
def chrome_options():
    """
    Return the chrome options
    """
    options = webdriver.ChromeOptions()
    mobile_emulation = {"deviceName": "Nexus 5"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--no-sandbox")
    # options.add_argument("--headless")  # Run Chrome in headless mode
    # options.add_argument("--disable-dev-shm-usage")  # Avoid shared memory issues
    # options.add_argument("--disable-gpu")  # Fix some headless rendering issues
    options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )  # Avoid detection
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.cookies": 2  # 1=Allow, 2=Block
    })
    return options


@allure.title("Create and setup chrome driver")
@pytest.fixture(name="driver_setup", scope="class")
def create_driver(get_chrome_options):
    """
    Create and setup driver
    """
    options = get_chrome_options
    driver = webdriver.Chrome(service=Service(), options=options)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True, scope="function")
def teardown_tests(request):
    """
    Teardown tests (On function level)
    Make and attach the screenshot to the allure report for failed tests
    """
    old_fails = request.session.testsfailed
    yield
    if request.session.testsfailed > old_fails:
        values = []
        test_name = request.node.originalname
        if hasattr(request.node, "callspec"):
            values = request.node.callspec.params.values()
        params = f"({'-'.join(filter(None, values))})"
        name = f"{test_name + params}.png"
        allure.step("Sanitize the screenshot name")
        name = re.sub(r'[<>:"/|?*]', "-", name)
        sanitized_name = re.sub(r"-{2,}", "-", name)

        if hasattr(request.cls, "driver"):
            driver: webdriver = request.cls.driver
            driver.save_screenshot(sanitized_name)
            allure.attach.file(
                sanitized_name,
                name=sanitized_name,
                attachment_type=allure.attachment_type.PNG,
            )
