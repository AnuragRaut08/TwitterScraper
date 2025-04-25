# TwitterScraper


This project is developed to scrape the top 5 trending topics from Twitter's "What’s Happening" section using **Selenium** and **ProxyMesh**, store the scraped data in a **MongoDB** database, and display the results on a simple web UI powered by **Flask**.

---

## **Features**
- Automates the process of logging into Twitter and fetching the top 5 trending topics.
- Ensures anonymity by routing requests through ProxyMesh, using a different IP address for each session.
- Stores the scraped data in MongoDB with a unique ID, timestamp, IP address used, and the trending topics.
- Displays the results on a simple HTML webpage.
- Provides a JSON view of the stored record for easy reference.

---

## **Technologies Used**
1. **Python**: Programming language for scripting and backend.
2. **Selenium**: For web scraping and browser automation.
3. **MongoDB**: NoSQL database for storing scraped data.
4. **Flask**: Lightweight web framework for creating the interface.
5. **ProxyMesh**: Proxy service for routing requests through different IPs.

---

## **Prerequisites**
Before running this project, ensure you have:
1. Python 3.6 or above installed.
2. MongoDB installed locally or access to a MongoDB Atlas cluster.
3. Google Chrome browser installed.
4. `chromedriver` compatible with your Chrome version ([Download here](https://chromedriver.chromium.org/)).
5. A Twitter account with valid credentials.
6. ProxyMesh account with proxy credentials.

---

## **Setup Instructions**
### 1. Clone the Repository
```bash
git clone https://github.com/AnuragRaut08/TwitterScraper.git
cd TwitterScraper
```

### 2. Install Dependencies
Install all required Python packages using the provided `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Configure Proxy and Credentials
- Open `selenium_script.py` and update the following:
  - Proxy credentials (`PROXY` variable):
    ```python
    PROXY = "http://username:password@proxy.proxyMesh.com:port"
    ```
  - Twitter login credentials:
    ```python
    username = "your_twitter_username"
    password = "your_twitter_password"
    ```

### 4. Set Up MongoDB
1. Ensure MongoDB is running locally, or set up a cloud database (e.g., MongoDB Atlas).
2. Update the MongoDB connection string in both `selenium_script.py` and `app.py` if necessary:
   ```python
   mongo_client = MongoClient("mongodb://localhost:27017/")
   ```

### 5. Run the Flask App
Start the Flask application:
```bash
python app.py
```

---

## **Usage**
1. Open your browser and navigate to `http://127.0.0.1:5000`.
2. Click **"Click here to run the script"** to start scraping.
3. View the results, including:
   - Top 5 trending topics.
   - Date and time of the scraping.
   - The IP address used for the request.
   - JSON extract of the MongoDB record.

---

## **Folder Structure**
```
twitter_trends_scraper/
│
├── app/
│   ├── __init__.py                   # Initialize Flask app
│   ├── routes.py                     # Define routes for the app (Flask)
│   ├── static/
│   │   └── style.css                 # Custom CSS for frontend styling
│   ├── templates/
│   │   └── index.html                # Main HTML template with buttons and results
│   └── dash_app.py                   # Dash app for data visualization
│
├── scripts/
│   ├── twitter_scraper.py            # Selenium scraper script with proxy rotation
│   ├── analysis.py                   # Script for data analysis and categorization
│   └── database_connector.py         # MongoDB connection setup
│
├── data/
│   └── trend_analysis.csv            # Analysis results saved from the database
│
├── requirements.txt                 # Python dependencies
├── Procfile                         # For Heroku deployment
├── README.md                        # Project documentation
└── .gitignore                       # Ignore unnecessary files/folders (e.g., virtualenv, logs)


---

## **Example Output**
### **HTML Page**
```
These are the most happening topics as on 2025-01-22 18:30:00:
1. Trend 1
2. Trend 2
3. Trend 3
4. Trend 4
5. Trend 5

The IP address used for this query was 123.45.67.89.

JSON Extract:
{
    "_id": "unique_id",
    "nameoftrend1": "Trend 1",
    "nameoftrend2": "Trend 2",
    "nameoftrend3": "Trend 3",
    "nameoftrend4": "Trend 4",
    "nameoftrend5": "Trend 5",
    "timestamp": "2025-01-22 18:30:00",
    "ip_address": "123.45.67.89"
}
```

---

## **Troubleshooting**
- **ChromeDriver Compatibility**: Ensure your ChromeDriver version matches your installed Google Chrome version.
- **ProxyMesh Setup**: Confirm your ProxyMesh credentials and IP access settings are correctly configured.
- **Twitter Login Issues**: Verify your Twitter account credentials are correct and not blocked by Twitter.
- **MongoDB Connection**: Check that your MongoDB instance is running and accessible.

---

## **Future Enhancements**
- Add pagination to view multiple scraped records from MongoDB.
- Implement error handling for failed proxy connections or Selenium exceptions.
- Expand scraping functionality to include additional sections of the Twitter homepage.

---

## **Author**
-Anurag Raut
-anuragtraut2003@gmail.com
-Connect on https://linkedin.com/in/anurag-raut-338b8b2b8
