from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the webdriver
# Note: You have to allow the Safari 
# To enable the 'Allow Remote Automation' option in Safari's Develop menu,
driver = webdriver.Safari()
shimmy = "https://shimmy-rukundo.github.io/bio/"


# Navigate to the blog page
driver.get(shimmy)

# Find all of the links on the page
links = driver.find_elements(By.TAG_NAME, 'a')
# Iterate through the links and click on each one
for link in links: 
    try:
        link.click()
        # Wait for the page to load
        driver.implicitly_wait(10)
        # Print the title of the page
        print(driver.title, driver.current_url, driver.execute_script(
            "return document.readyState"))
        if driver.current_url.startswith(shimmy):
            # The link does not return a 404 error
            print("The link does not return a 404 error.")
    except:
        print(driver.current_url ," == Error: Link did not lead to a valid page")
        
        
    # Navigate back to the blog page
    driver.get(shimmy)

# Quit the webdriver
driver.quit()
