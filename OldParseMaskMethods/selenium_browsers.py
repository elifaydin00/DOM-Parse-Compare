import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
"""
import lxml.html as lh
import lxml.html.clean as clean
content=browser_chrome.page_source
cleaner=clean.Cleaner()
content=cleaner.clean_html(content) 
doc=lh.fromstring(content)
print(doc)
"""


def getSiteSelenium(content_url):
    url = content_url
    #Chrome
    browser_chrome = webdriver.Chrome('./chromedriver')
    browser_chrome.get(url)

    soup = BeautifulSoup(browser_chrome.page_source, 'html.parser')
    browser_chrome.close()

    lists =[]
    print([tag.name for tag in soup.find_all()])


    print(lists)

    print("\n DONE CHROME\n")
    #Firefox
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.get(url)

    soup_firefox = BeautifulSoup(browser.page_source, 'html.parser')
    browser.close()

    lists_firefox =[]
    print([tag.name for tag in soup_firefox.find_all()])

    print(lists_firefox)

    
if __name__ == '__main__':
    content_url = "https://www.google.com/"
    getSiteSelenium(content_url)
