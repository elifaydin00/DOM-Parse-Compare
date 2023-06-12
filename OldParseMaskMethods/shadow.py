import os

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

#url: http://watir.com/examples/shadow_dom.html

def chrome_shadow():
    """Please use this code."""

    driver = Chrome()

    driver.get('http://watir.com/examples/shadow_dom.html')

    shadow_host = driver.find_element(By.CSS_SELECTOR, '#shadow_host')
    shadow_root = shadow_host.shadow_root
    shadow_content = shadow_root.find_element(By.CSS_SELECTOR, '#shadow_content')

    assert shadow_content.text == 'some text'

    driver.quit()


def firefox_shadow():
    """Firefox is special."""

    driver = Firefox()

    driver.get('http://watir.com/examples/shadow_dom.html')

    shadow_host = driver.find_element(By.CSS_SELECTOR, '#shadow_host')
    children = driver.execute_script('return arguments[0].shadowRoot.children', shadow_host)

    shadow_content = next(child for child in children if child.get_attribute('id') == 'shadow_content')

    assert shadow_content.text == 'some text'

    driver.quit()

chrome_shadow()
firefox_shadow()