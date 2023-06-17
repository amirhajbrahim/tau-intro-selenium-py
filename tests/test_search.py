"""
These tests cover DuckDuckGo searches
"""

from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage

def test_basic_duckduckgo_search(browser):

    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    Phrase = "Panda"

    # Given the DuckDuckGo home is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(Phrase)

    # Then the search result title contains "panda"
    assert Phrase in result_page.title()

    # And the search result query is "panda"
    assert Phrase == result_page.search_input_value()

    # And the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [title for title in titles if Phrase.lower() in title.lower()]
    assert len(matches) > 0

    # TODO: Remove this exception once the test is complete
    # raise Exception("Incomplete Test")
