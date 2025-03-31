"""Base class for common actions with webdriver"""

from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from resources.general.global_variables import GlobalVariables
from resources.general.locators import Locators
from resources.general.custom_wait import CustomWait


class BaseClass(CustomWait):
    """
    Base class for work with browser application
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(driver)
        self.glob = GlobalVariables()
        self.loc = Locators()
        self.keys = Keys

    def set_field(self, element, value):
        """
        Set value to the field
        """
        field = self.wait_clickable(element, f"No element {element} located")
        field.send_keys(self.keys.CONTROL + "a")
        field.send_keys(value)
        assert (
            field.get_attribute("value") == value
        ), f"Field {element} is not filled with value {value}"

    def is_element_exist(self, element):
        """
        Check if element exist, and return obj or False
        """
        try:
            if isinstance(element, WebElement):
                return self.ec.visibility_of(element)
            return self.driver.find_element(*element)
        except (NoSuchElementException, StaleElementReferenceException):
            return False
