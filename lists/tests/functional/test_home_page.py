from django.test import LiveServerTestCase
from selenium import webdriver

class HomePageTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_displays_input_prompt(self):
        self.browser.get(self.live_server_url)

        body_text = self.browser.find_element("tag name", "body").text
        self.assertIn("Enter a to-do item", body_text)

    def test_home_page_has_input_box(self):
        self.browser.get(self.live_server_url)

        inputbox = self.browser.find_element("name", "item_text")
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter a to-do item"
        )
