import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient
import time
import uuid
import requests


# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client["twitter_trends"]
collection = db["trends"]

# Function to scrape data from Twitter
def scrape_twitter(proxy):
    options = webdriver.ChromeOptions()
    options.add_argument(f'--proxy-server={proxy}')
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(options=options)

    try:
        # Log in to Twitter
        driver.get("https://twitter.com/login")
        time.sleep(5)
        username = driver.find_element(By.NAME, "session[username_or_email]")
        password = driver.find_element(By.NAME, "session[password]")
        username.send_keys("your_username")
        password.send_keys("your_password")
        password.send_keys(Keys.RETURN)
        time.sleep(10)

        # Scrape trending topics
        driver.get("https://twitter.com/home")
        time.sleep(5)
        trends = driver.find_elements(By.XPATH, "//div[@data-testid='trend']")[:5]

        results = [trend.text for trend in trends]

        # Generate a unique ID and get the current IP address
        unique_id = str(uuid.uuid4())
        ip_address = requests.get("https://api.ipify.org").text

        # Insert results into MongoDB
        data = {
            "_id": unique_id,
            "trend1": results[0] if len(results) > 0 else None,
            "trend2": results[1] if len(results) > 1 else None,
            "trend3": results[2] if len(results) > 2 else None,
            "trend4": results[3] if len(results) > 3 else None,
            "trend5": results[4] if len(results) > 4 else None,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "ip_address": ip_address,
        }
        collection.insert_one(data)
        print(f"Data inserted with ID: {unique_id}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

# List of proxy servers (Replace these with actual ProxyMesh proxies)
proxies = [
    "http://proxy1.example.com:8080",
    "http://proxy2.example.com:8080",
    "http://proxy3.example.com:8080",
]

# Run scraping asynchronously
if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(scrape_twitter, proxies)
