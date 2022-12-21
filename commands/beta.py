from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Set up the webdriver
driver = webdriver.Safari()
shimmy = "https://shimmy-rukundo.github.io/home/"

# Navigate to the webpage
driver.get(shimmy)

# Find all of the links on the page
links = driver.find_elements(By.TAG_NAME, "a")

# Iterate over the links
for link in links:
    url = (link.get_attribute("href"))
    
    # Send an HTTP request to the webpage
    response = requests.get(url)
    # Check the status code
    if response.status_code == 404:
        # The webpage was not found
        print("NOT FOUND =||= ", url)
    else:
        # The webpage was found
        print("FOUND =||= ", url)
# Close the webdriver
driver.quit()
