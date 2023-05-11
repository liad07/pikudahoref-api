from flask import Flask, jsonify
import time
import json
from selenium import webdriver

from bs4 import BeautifulSoup

app = Flask(__name__)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

prev_alert_dates = set()
i=0

@app.route("/")
def get_new_alerts():
    global prev_alert_dates
    global i

    driver.get("https://www.oref.org.il/WarningMessages/History/AlertsHistory.json")
    page_source = driver.page_source
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # Do something with the JSON data
    json_data = (json.loads(soup.text))
    # Close the driver

    new_alerts = [alert for alert in json_data if alert["alertDate"] not in prev_alert_dates]

    if new_alerts:
        prev_alert_dates.update(alert["alertDate"] for alert in new_alerts)

        if i>0:
            print(new_alerts)
            return jsonify(new_alerts)

        else:
            i += 1
            return jsonify([])

    else:
        return jsonify(["no alerts"])


if __name__ == "__main__":
    app.run()
