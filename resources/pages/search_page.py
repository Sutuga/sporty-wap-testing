import allure
from resources.pages.common_page import CommonPage


class SearchPage(CommonPage):
    """
    Class for Search Page functionality
    """

    @allure.step("Search {browse_text} by 'Browse' button")  # exaple of allure step
    def browse(self, browse_text: str):
        """
        Search on the main page
        """
        self.wait_clickable(self.loc.browse_btn, "No 'Browse' button located").click()
        search = self.wait_clickable(self.loc.search_field, "No search field located")
        self.set_field(search, browse_text)
        search.send_keys(self.keys.ENTER)

    def select_tab(self, tab_name):
        """
        Select tab by name
        """
        tab = self.wait_clickable(
            self.loc.search_tab.val(tab_name), f"Can`t click on the tab - {tab_name}"
        )
        tab.click()
        assert tab.text == tab_name, f"Selected wrong tab {tab.text}"
        self.wait_page_loaded()

    def select_stream_by_channel_name(self, channel_name: str):
        """
        Select stream by channel name
        """
        self.wait_clickable(
            self.loc.stream_title.val(channel_name),
            f"No element with title '{channel_name}' on the page",
        ).click()

    def select_channel_in_list(self, channel_name=None):
        """
        Select channel in the list (first loaded) Could be updated for use channel_name
        """
        target = self.wait_text_not_empty(
            self.loc.stream_elements_btn, "Empty text for object"
        )
        channel_name = self.wait_child(target, self.loc.common_title).text
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'})", target
        )
        self.wait_page_loaded()
        print(f"Channel name for select is {channel_name}")
        self.select_stream_by_channel_name(channel_name)
        return channel_name
