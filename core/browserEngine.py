import re
import os
import sys
from core.config import xsschecker
from core.utils import writer
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def browserEngine(response):
    #cap = DesiredCapabilities().FIREFOX
    #cap["marionette"] = False
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    #browser = webdriver.Firefox(capabilities=cap, options=options, executable_path="/usr/share/webapps/XSStrike/geckodriver/geckodriver")
    #browser.get('http://google.com/')
    #browser.quit()
    response = re.sub(r'<script.*?src=.*?>', '<script src=#>', response, re.I)
    response = re.sub(r'href=.*?>', 'href=#>', response, re.I)
    writer(response, 'test.html')
    browser.get('file://' + sys.path[0] + '/test.html')
    os.remove('test.html')
    popUp = False
    actions = webdriver.ActionChains(browser)
    try:
        actions.move_by_offset(2, 2)
        actions.perform()
        browser.close()
    except UnexpectedAlertPresentException:
        popUp = True
        browser.quit()
    return popUp
