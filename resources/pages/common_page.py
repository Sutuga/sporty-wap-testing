import os
import allure
from resources.general.base_class import BaseClass


class CommonPage(BaseClass):
    """
    Class for common pages logic
    """

    def accept_policy(self):
        """
        Accept general policy (this method could move to
        a separate class (modal wnd) if amount of the methods increased)
        """
        self.wait_clickable(
            self.loc.accept_policy_btn, "Setting button not clickable"
        ).click()

    def scroll_page(self, times: int = 1):
        """
        Scroll the page for full screen height by number of times
        :param times: How many times to scroll
        """
        for _ in range(times):
            self.actions.send_keys(self.keys.PAGE_DOWN).perform()
            self.wait_page_loaded()

    def take_screenshot(self, text=None):
        """
        Make png a screenshot of the page with text
        """
        scr_path = f"../tests/screenshots/{text}.png"
        self.driver.save_screenshot(scr_path)
        allure.attach.file(
            scr_path,
            name=text,
            attachment_type=allure.attachment_type.PNG,
        )
        os.remove(scr_path)
        return scr_path

    def wait_page_loaded(self):
        """
        Wait for page to be loaded by conditions (elements are present, visible, etc.)
        """
        count = self.wait_obj_located(self.loc.video_list).get_attribute(
            "childElementCount"
        )
        self.wait_elements_count_to_be(self.loc.stream_elements_btn, int(count))
        self.wait_doc_complete()
        self.wait_all_elements_visible(self.loc.full, "Channel name not visible")
        self.wait_text_not_empty(self.loc.stream_elements_btn, "Empty text for object")
