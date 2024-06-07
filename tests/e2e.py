from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import sys

def test_scores_service(app_url):
    try:
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')  # Run in headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # Use GeckoDriverManager to install the driver
        service = FirefoxService(executable_path=GeckoDriverManager().install())

        driver = webdriver.Firefox(service=service, options=options)
        driver.get(app_url)

        # Find the score element by ID
        score_element = driver.find_element(By.ID, 'score')
        score_value = int(score_element.text)
        result = 1 <= score_value <= 1000
        return bool(result)
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        if 'driver' in locals():
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
