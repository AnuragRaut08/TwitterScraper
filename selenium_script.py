from flask import Flask, render_template
from pymongo import MongoClient
import subprocess

app = Flask(__name__)

# MongoDB setup
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["twitter_data"]
collection = db["trending_topics"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_script")
def run_script():
    # Run the Selenium script
    subprocess.run(["python", "selenium_script.py"])  # Ensure selenium_script.py is in the same folder
    latest_record = collection.find_one(sort=[("timestamp", -1)])
    return render_template("results.html", record=latest_record)

if __name__ == "__main__":
    app.run(debug=True)
