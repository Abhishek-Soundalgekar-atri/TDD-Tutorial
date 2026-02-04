from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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

    def test_user_can_enter_a_todo_item(self):
        self.browser.get(self.live_server_url)

        inputbox = self.browser.find_element("name", "item_text")
        inputbox.send_keys("Buy milk")
        inputbox.send_keys(Keys.ENTER)

        list_items = self.browser.find_elements("css selector", "#id_list li")
        self.assertIn("Buy milk", [item.text for item in list_items])


