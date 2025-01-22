import time
import uuid
from selenium import webdriver
from selenium.webdriver.common.by import By
from pymongo import MongoClient
import requests

# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client["twitter_trends"]
collection = db["trends"]

def scrape_twitter(proxy):
    options = webdriver.ChromeOptions()
    options.add_argument(f'--proxy-server={proxy}')
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://twitter.com/login")
        # Login process here
        # Scraping code here for top 5 trends
        trends = driver.find_elements(By.XPATH, "//div[@data-testid='trend']")[:5]
        results = [trend.text for trend in trends]

        unique_id = str(uuid.uuid4())
        ip_address = requests.get("https://api.ipify.org").text

        data = {
            "_id": unique_id,
            "trend1": results[0],
            "trend2": results[1],
            "trend3": results[2],
            "trend4": results[3],
            "trend5": results[4],
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "ip_address": ip_address,
        }
        collection.insert_one(data)
        print(f"Data inserted with ID: {unique_id}")
    finally:
        driver.quit()
