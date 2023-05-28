from playwright.sync_api import sync_playwright
import asyncio
# datetimeモジュールを使用
import datetime
import random

def run(playwright):

    pageurl = "https://forms.office.com/pages/responsepage.aspx?id=jahuGWvCBkS1GSb6HqTUJo9QcvBIK9REsOVvftMW2cNUQVJQODBSSE1JNFk3VlhENEI2RU5CSlM1SS4u"

    # 36.4から36.7まで0.1刻みのリストを作成
    nums = [round(i * 0.1, 1) for i in range(364, 368)]

    # リストからランダムに選択
    random_choice = random.choice(nums)

    # 日付
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    datestring = now.strftime('%Y/%m/%d %H:%M')



    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch()
    page = browser.new_page()
    page.set_viewport_size({"width": 720, "height": 1024})
    page.goto(pageurl)

    page.locator("input[aria-label='Single line text']").nth(0).fill("Ryo")
    page.locator("input[aria-label='Single line text']").nth(1).fill(str(random_choice))
    page.locator("input[type=radio]").nth(0).check()
    page.locator("input[aria-label='Single line text']").nth(2).fill(datestring)

    page.screenshot(path='./static/report.png', full_page=True)

    browser.close()

with sync_playwright() as playwright:
    run(playwright)