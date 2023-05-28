import re

from playwright.sync_api import Page, expect

def test_playwright(page: Page):
    pageurl = "https://forms.office.com/pages/responsepage.aspx?id=jahuGWvCBkS1GSb6HqTUJo9QcvBIK9REsOVvftMW2cNUQVJQODBSSE1JNFk3VlhENEI2RU5CSlM1SS4u"

    page.goto(pageurl)
    # page.screenshot(path="screenshot.png", full_page=True)
    page.locator("div#question-list").screenshot(path="screenshot.png")



