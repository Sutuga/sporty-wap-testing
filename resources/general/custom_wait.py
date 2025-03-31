from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from resources.general import custom_conditions as cc


class CustomWait:
    """
    Class for custom waits functionality
    Also could be present some custom conditions for extending
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.ec = expected_conditions

    def wait_obj_located(self, locator, msg: str = ""):
        """
        Wait and return the web element object
        """
        return self.wait.until(self.ec.presence_of_element_located(locator), message=msg)

    def wait_visible_located(self, locator, msg: str = ""):
        """
        Wait object (locator) is present and visible in DOM model
        """
        return self.wait.until(
            self.ec.visibility_of_element_located(locator), message=msg
        )

    def wait_clickable(self, locator, msg: str = ""):
        """
        Wait object is clickable
        """
        return self.wait.until(self.ec.element_to_be_clickable(locator), message=msg)

    def wait_elements_count_to_be(self, locator, count: int):
        """
        Wait for exactly count of elements
        """
        return self.wait.until(
            cc.elements_count_to_be(locator, count),
            message=f"Count not equal {str(count)}",
        )

    def wait_child(self, parent, locator):
        """
        Wait child exist in the parent
        """
        return self.wait.until(lambda d: parent.find_element(*locator))

    def wait_doc_complete(self):
        """
        Wait for document to be completely loaded
        """
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def wait_text_not_empty(self, locator, msg: str = ""):
        """
        Wait for text not empty
        """
        return self.wait.until(cc.text_not_empty(locator), message=msg)

    def wait_all_elements_visible(self, locator, msg: str = ""):
        """
        Wait for all elements visible
        """
        return self.wait.until(
            self.ec.visibility_of_all_elements_located(locator), message=msg
        )
