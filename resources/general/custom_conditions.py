from selenium.common.exceptions import StaleElementReferenceException


def elements_count_to_be(locator, count: int):
    """Custom expected condition to wait for exactly N elements"""

    def _predicate(driver):
        elements = driver.find_elements(*locator)
        return len(elements) == count if elements else False

    return _predicate


def text_not_empty(locator):
    """Custom expected condition to check if text is not empty"""

    def _predicate(driver):
        try:
            element = driver.find_element(*locator)
            if element.text != "":
                return element
        except StaleElementReferenceException:
            return False
        return False

    return _predicate
