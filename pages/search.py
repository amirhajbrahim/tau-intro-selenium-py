"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from selenium.webdriver.common.by import By

class DuckDuckGoSearchPage:

    # URL
    URL = "https://duckduckgo.com/"
    # Locators
    SEARCH_INPUT = (By.ID, 'searchbox_input')
    SEARCH_BUTTON = (By.XPATH, "//div[@class='searchbox_iconWrapper__suWUe']/button[1]")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_input.send_keys(phrase)
        search_button.click()