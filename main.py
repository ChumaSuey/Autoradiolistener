from playwright.sync_api import sync_playwright
import asyncio
import time as t

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.wait_for_load_state()

    t.sleep(250)
async def click_button(page):
    await page.click('text="Acceptä tot"');

    # Type in the search bar
    page.fill("input[name='q']", "circuito lider")

    # Submit the search form
    page.press("input[name='q']", "Enter")

    # Wait for the search results to load
    page.wait_for_load_state()

    # Click on the first link
    page.click("a[href='https://circuitolider.com']")

    # Keep the browser open
    # (no browser.close)