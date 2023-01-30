from selenium.webdriver.common.keys import Keys

from functional_tests.home_page_ft_base import HomePageFT


class SeveralVisitorsTest(HomePageFT):
    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)
        input_box = self.browser.find_element_by_id("id_new_item")
        input_box.send_keys("Buy peacock feathers")
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # She notices that her list has a unique url
        self.edith_list_url = self.browser.current_url
        self.assertRegex(self.edith_list_url, '/lists/.+')

    def test_new_user_do_not_see_previous_lists(self):
        self.create_list_for_francis()
        # Francis visits the home page.  There is no sign of Edith's
        # list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesting than Edith...
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Buy milk')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, self.edith_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

    def create_list_for_francis(self):
        self.browser.get(self.live_server_url)
        input_box = self.browser.find_element_by_id("id_new_item")
        input_box.send_keys("Buy peacock feathers")
        input_box.send_keys(Keys.ENTER)
