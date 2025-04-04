from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Set up the WebDriver
service = Service(r'C:\Users\LENOVO\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')  # Update with your path to chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Step 1: Launch the Chrome browser
print("Launching the browser and navigating to the Tatsumeeko site...")
driver.get("https://tatsu.works")

# Step 2: Wait for the page to load completely
print("Waiting for the page to load completely...")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
print("Page loaded.")

# Step 3: Locate the "Tatsumeeko" button
print("Locating the 'Tatsumeeko' button...")
tatsumeeko_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@id="comp-k62bplnq"]//a[@aria-label="TATSUMEEKO"]'))
)
print("Tatsumeeko button located.")

# Step 4: Verify that the button is visible and enabled
assert tatsumeeko_button.is_displayed() and tatsumeeko_button.is_enabled()
print("Tatsumeeko button is visible and enabled.")

# Step 5: Click the "Tatsumeeko" button
print("Clicking the Tatsumeeko button...")
tatsumeeko_button.click()
print("Button clicked, waiting for the Tatsumeeko homepage to load...")

# Step 6: Switch to the new tab
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
driver.switch_to.window(driver.window_handles[1])

# Step 7: Print the current URL for debugging
print("Current URL after switching to new tab:", driver.current_url)

# Step 8: Verify that a specific element on the Tatsumeeko homepage is present
WebDriverWait(driver, 40).until(
    EC.presence_of_element_located((By.XPATH, '//img[@alt="tatsumeeko logo"]'))  # Update with the correct XPath for an element on the Tatsumeeko homepage
)
print("Tatsumeeko web opened successfully.")

# Postcondition: Close the browser
print("Closing the browser.")
driver.quit()