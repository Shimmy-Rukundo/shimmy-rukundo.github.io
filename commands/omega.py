import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the webdriver
driver = webdriver.Safari()
shimmy = "https://shimmy-rukundo.github.io/bio/"

# Navigate to the blog page
driver.get(shimmy)

# Find all of the links on the page
links = driver.find_elements(By.TAG_NAME, "a")

# Iterate over the links
for link in links:
    # Navigate to the link
    driver.get(link.get_attribute("href"))

    # Check the current URL
    if driver.current_url.startswith(link.get_attribute("href")):
        # The link does not return a 404 error
        print(f"{link.get_attribute('href')}: The link does not return a 404 error.")
        # Get the title of the page
        print(f"Title: {driver.title}")
    else:
        # The link returns a 404 error
        print(f"{link.get_attribute('href')}: The link returns a 404 error.")

# Close the webdriver
driver.quit()
