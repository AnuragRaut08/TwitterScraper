from flask import Blueprint, render_template, jsonify
from scripts.twitter_scraper import scrape_twitter
from scripts.database_connector import get_latest_trends

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def index():
    return render_template('index.html')

@app_routes.route('/run_scraper')
def run_scraper():
    # Call the scraping function (you can add logic to call asynchronously)
    scrape_twitter("http://proxy1.example.com:8080")
    
    # Fetch the latest results from MongoDB
    latest_data = get_latest_trends()
    
    return render_template('index.html', data=latest_data)
