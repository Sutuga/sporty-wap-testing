from selenium.webdriver.common.by import By


class Dynamic:
    """
    Using for dynamically changing locators by sending value.
    By default, we will use the mask "dynamic-test-value" for the locator.
    The value will be inserted in the mask "dynamic-test-value""
    """

    mask = "dynamic-test-value"

    def __init__(self, way, locator):
        self.way = way
        self.locator = locator

    def val(self, value):
        """
        Return the locator with the new value
        """
        return self.way, self.locator.replace(self.mask, value)


class Locators:
    """
    All locators for the project
    """

    # General
    accept_policy_btn = (By.CSS_SELECTOR, "button[data-a-target$=accept]")
    browse_btn = (By.XPATH, "//div[text()='Browse']")

    # Search Page
    search_field = (By.CSS_SELECTOR, "input[type='search']")
    stream_elements_btn = (By.CSS_SELECTOR, "[class*='CoreLink']")
    search_tab = Dynamic(By.XPATH, "//a[normalize-space()='dynamic-test-value']")
    stream_title = Dynamic(By.CSS_SELECTOR, "button:has(h2[title='dynamic-test-value'])")
    common_title = (By.CSS_SELECTOR, "h2")
    full = (By.CSS_SELECTOR, "[class*='CoreLink'] h2")
    video_list = (By.CSS_SELECTOR, "[role='list']")
    main_content = (By.CSS_SELECTOR, "[aria-label*='Main']")
    navigation_header = (By.CSS_SELECTOR, main_content[1] + ">nav")
    avatar = Dynamic(By.CSS_SELECTOR, "button[aria-label*='dynamic-test-value']")

    # Video Page
    content_overlay = (
        By.CSS_SELECTOR,
        "button[data-a-target*='content-classification-gate-overlay']",
    )

    # Channel Page
    channel_page = (By.ID, "page-main-content-wrapper")
    channel_avatar = (By.CSS_SELECTOR, "img[class*='avatar']")
    channel_content = (By.CSS_SELECTOR, "[srcset]")
