from playwright.sync_api import sync_playwright
import asyncio

def search_google(query):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = browser.new_page()
        page.goto("https://www.google.com")
        page.type('[role="combobox"]', query)
        page.wait_for_timeout(1000)
        page.keyboard.press("Enter")
        page.wait_for_timeout(5000)
        # Navigate to the relative path
        relative_path = "//div[@class='tF2Cxc']//div[@class='yuRUbf']//div//h3[@class='LC20lb MBeuO DKV0Md'][contains(text(),'Circuito Líder')]"
        result = page.query_selector(relative_path)
        if result:
            result.click()
        else:
            print("Could not find the result")
        page.wait_for_timeout(5000)
        # Click on the play button
        play_button = page.query_selector("//img[@id='boton-play-pause']")
        if play_button:
            play_button.click()
        else:
            print("Could not find the play button")
        # Pause for 10 seconds
        page.wait_for_timeout(10000)
        browser.close()

if __name__ == "__main__":
    search_google("Circuito Lider")