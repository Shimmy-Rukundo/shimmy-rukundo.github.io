import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the webdriver
driver = webdriver.Safari()
shimmy = "https://shimmy-rukundo.github.io/bio/"

# Navigate to the webpage
driver.get(shimmy)

# Find all of the links on the page
links = driver.find_elements(By.TAG_NAME, "a")

# Iterate over the links
for link in links:
    print(link.get_attribute("href"))

# Close the webdriver
driver.quit()
