from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

itc_hs_code = 842112
url = f"https://www.macmap.org/en/query/results?reporter=842&partner=699&product={itc_hs_code}&level=6"

# Set up Chrome options to run headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--no-sandbox")  # Required for some environments
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Initialize the Chrome driver with options
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Wait for the page to load and locate the search button
try:
    # Adjust the locator method to find the actual search button on the page
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit"))  # Replace with the actual button ID or selector
    )
    search_button.click()  # Click the search button

    # Wait for results to load, then scrape as needed
    results = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "main-content"))  # Replace with actual ID or class name of result container
    )

    # Extract and print the data
    print("Results:", results.text)

except Exception as e:
    print("An error occurred:", e)

# Close the driver after completing
driver.quit()
