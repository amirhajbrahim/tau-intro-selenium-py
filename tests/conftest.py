"""
This module contains shared fixtures.
"""

import pytest
import selenium.webdriver
import json
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def config(scope='session'):

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config

@pytest.fixture
def browser(config):

    # initialize the ChromeDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()

    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)

    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()
