from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_row_in_list(browser, text, timeout=10):
    WebDriverWait(browser, timeout).until(
        EC.text_to_be_present_in_element(
            (By.ID, "id_list"),
            text
        )
    )


