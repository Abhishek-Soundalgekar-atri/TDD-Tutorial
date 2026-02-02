from django.test import LiveServerTestCase
from selenium import webdriver

class HomePageTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_displays_input_prompt(self):
        # User opens the home page
        self.browser.get(self.live_server_url)

        # User sees an invitation to enter a to-do item
        body_text = self.browser.find_element("tag name", "body").text
        self.assertIn("Enter a to-do item", body_text)
