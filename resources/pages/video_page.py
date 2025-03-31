from resources.pages.common_page import CommonPage


class VideoPage(CommonPage):
    """
    Class for Feed page functionality
    """

    def open_streamer_page(self, channel_name=None):
        """
        Open streamer page by channel name (Click on the avatar)
        """
        self.wait_clickable(self.loc.avatar.val(channel_name)).click()
        self.wait_visible_located(self.loc.channel_page)
        self.wait_doc_complete()
        self.wait_visible_located(self.loc.channel_avatar)
        self.wait_all_elements_visible(self.loc.channel_content)

    def handle_content_overlay(self):
        """
        Handle content overlay, if it is present
        """
        if self.is_element_exist(self.loc.content_overlay):
            self.wait_clickable(self.loc.content_overlay).click()
            self.wait_doc_complete()
