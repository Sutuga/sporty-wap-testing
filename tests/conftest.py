"""provided basic functionality for tests suites"""

import allure
import pytest

from selenium.webdriver import Chrome
from resources.pages.search_page import SearchPage
from resources.pages.video_page import VideoPage
from resources.pages.home_page import HomePage
from resources.general.global_variables import GlobalVariables as gv


@allure.title("Inject all class references to the test class")
@pytest.fixture(name="_injector", scope="class")
def injector(request, driver_setup):
    """
    Define modules
    """
    driver: Chrome = driver_setup
    request.cls.driver = driver
    request.cls.search_page = SearchPage(driver)
    request.cls.video_page = VideoPage(driver)
    request.cls.home_page = HomePage(driver)
    request.cls.glob = gv


@pytest.fixture(scope="class")
def run_application(request, _injector):
    """
    Prepare browser for test. Open additional tab.
    """
    r = request.cls
    allure.step(f"Run application - {gv.APP}")
    r.driver.get(gv.APP)
    r.home_page.accept_policy()
