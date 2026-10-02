"""
basic example of browser automation (filling out forms, click buttons, etc) using playwright
"""

from playwright.sync_api import sync_playwright

START_URL = "https://amazon.com"

# open a browser and navigate to the start url
with sync_playwright() as p:
    # you can change this to p.firefox or p.webkit if you want to use a different browser
    # headless=False means that the browser will be visible, set it to True if you want to run it in the background
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(START_URL)

    # fill out the search form and submit it
    page.fill("input[name='field-keywords']", "test")
    page.click("input[type='submit']")

    # close the browser
    browser.close()
