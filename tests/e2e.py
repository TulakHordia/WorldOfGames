from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
import sys
import time

def test_scores_service(app_url):
    try:
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')  # Run in headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # Use installed GeckoDriver path
        service = FirefoxService(executable_path='/usr/local/bin/geckodriver')

        driver = webdriver.Firefox(service=service, options=options)
        print(f"Opening URL: {app_url}")
        driver.get(app_url)

        time.sleep(5)  # Wait for the page to load

        # Find the score element by ID
        print("Finding element by ID: 'score'")
        score_element = driver.find_element(By.ID, 'score')
        print(f"Element found: {score_element.text}")
        score_value = int(score_element.text)
        result = 1 <= score_value <= 1000
        print(f"Test result: {result}")
        return bool(result)
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        if 'driver' in locals():
            print("Quitting driver")
            driver.quit()

def main_function():
    # Updated to match the Flask app port
    app_url = "http://127.0.0.1:8777/"

    if test_scores_service(app_url):
        print("Test passed")
        sys.exit(0)
    else:
        print("Test failed")
        sys.exit(-1)

if __name__ == "__main__":
    main_function()
