from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Set up the webdriver
driver = webdriver.Chrome()  # Replace with your preferred browser

def pause(pv):
    time.sleep(pv)

def close(driver):
    driver.close()

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
    link_xpath = "//h3[text()='Circuito Líder']"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, link_xpath)))

    # Click on the first link
    first_link = driver.find_element(By.XPATH, link_xpath)
    first_link.click()


def play_button(driver):
    # Find the play button element by its ID
    play_button = driver.find_element(By.ID, 'boton-play-pause')

    # Click the play button
    play_button.click()

find_website(driver)
click_button(driver)
pause(10)
play_button(driver)
pause(20)
close(driver)
