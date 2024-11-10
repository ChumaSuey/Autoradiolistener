from playwright.sync_api import sync_playwright
import asyncio
import time as t

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.set_geolocation(None)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.type('[role="combobox"]', "Circuito Lider")
    page.wait_for_timeout(1000)  # pause for 1 second
    page.keyboard.press("Enter")  # press Enter
    page.wait_for_timeout(5000)
    first_result = page.query_selector('div.tF2Cxc div.yuRUbf div h3.LC20lb.MBeuO.DKV0Md:has-text("Circuito Líder")')
     if first_result:
     page.click(first_result)  # click on the first search result
     else:
         print("Could not find the first search result")
    page.wait_for_timeout(5000)  # keep the browser open for 5 seconds