# pikudahoref api Alert Checker

This is a simple Flask application that uses Selenium and BeautifulSoup to scrape the OREF website for new alerts and returns them as JSON. The application runs in headless mode and checks for new alerts every time the root URL is accessed.

# Requirements
This application requires the following dependencies to be installed:

- Flask
- Selenium
- BeautifulSoup
# Installation
To install the dependencies, you can use pip:
``` bash
pip install flask selenium beautifulsoup4
```
You also need to have Chrome and ChromeDriver installed on your system.

# Usage
To run the application, simply run the following command:
``` bash
python app.py
```
This will start the Flask development server and the application will be accessible at http://localhost:5000.

When you access the root URL, the application will scrape the OREF website for new alerts and return them as JSON. The alerts will only be returned once, so subsequent requests will return an empty list until new alerts are available.

# License
This application is released under the MIT License. See LICENSE for details.
