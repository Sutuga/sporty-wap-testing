import pytest
import allure
from resources.scenarious.common_scenarios import CommonScenarios


@pytest.mark.usefixtures("run_application")
class TestSearchSuite(CommonScenarios):
    """
    Test suite for the wap tests
    """

    @allure.title("Search channel by text")
    def test_search_streamer_page(self):
        """
        User find and open streamer page
        """
        with allure.step("Search channel by text"):
            self.search_page.browse("StarCraft II")
            self.search_page.select_tab("Channels")
            self.search_page.scroll_page(2)
            channel = self.search_page.select_channel_in_list()
            self.video_page.handle_content_overlay()
            self.video_page.open_streamer_page(channel)

        screenshot_name = f"channel_name_{channel}"
        self.video_page.take_screenshot(screenshot_name)
