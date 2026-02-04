from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .helpers import wait_for_row_in_list



class HomePageTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_displays_input_prompt(self):
        self.open_home_page()


        body_text = self.browser.find_element("tag name", "body").text
        self.assertIn("Enter a to-do item", body_text)

    def test_home_page_has_input_box(self):
        self.open_home_page()


        inputbox = self.browser.find_element("name", "item_text")
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            "Enter a to-do item"
        )

    def test_user_can_enter_a_todo_item(self):
        self.open_home_page()


        inputbox = self.browser.find_element("name", "item_text")
        inputbox.send_keys("Buy milk")
        inputbox.send_keys(Keys.ENTER)

        wait_for_row_in_list(self.browser, "Buy milk")
        
    def open_home_page(self):
        self.browser.get(self.live_server_url)




