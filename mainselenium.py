from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Set up the webdriver
driver = webdriver.Chrome()  # Replace with your preferred browser

def find_website(driver):
# Navigate to Google
    driver.get("https://www.google.com")
# Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
# Wait for 5 seconds.
    time.sleep(5)

def click_button(driver):
    # Type in the search bar
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.send_keys("circuito lider")

    # Submit the search form
    search_bar.send_keys(Keys.RETURN)

    # Wait for the search results to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "rso")))

    # Wait for the link to be present on the page
    link_xpath = "//h3[contains(text(),'Circuito Líder - Fuerza Radial en Venezuela - stre')]"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, link_xpath)))

    # Click on the first link
    first_link = driver.find_element(By.XPATH, link_xpath)
    first_link.click()


def play_button(driver):
    # Wait for the play button to be present on the page
    play_button_css = ".btn.btn-play"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, play_button_css)))

    # Click on the play button
    play_button_element = driver.find_element(By.CSS_SELECTOR, play_button_css)
    play_button_element.click()

    time.sleep(10)

    # Keep the browser open
    # (no driver.quit)


find_website(driver)
click_button(driver)
play_button(driver)
time.sleep(10)
