from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

# Set the path to the HTML file
current_directory = os.path.dirname(os.path.abspath(__file__))
html_file_path = os.path.join(current_directory, "products.html")

# Set up the WebDriver and browser options
options = webdriver.ChromeOptions()
# Add any necessary browser options or configurations here
driver = webdriver.Chrome(options=options)

# Open the HTML file to be tested
driver.get("file:///" + html_file_path)

# Find the cart button element
cart_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cart-button")))

# Click the cart button
cart_button.click()

# Perform any other necessary actions and assertions for your functional tests
# For example, you can wait for the page to navigate to the cart.html
# wait = WebDriverWait(driver, 10)
# wait.until(EC.url_contains("cart.html"))

# You can also assert that certain elements or text are present on the page
assert "Items added to cart" in driver.page_source

# You can retrieve the current URL to verify the navigation
# current_url = driver.current_url
# assert current_url.endswith("cart.html")

# Clean up and close the WebDriver
driver.quit()
