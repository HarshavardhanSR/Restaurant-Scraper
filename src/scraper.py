import os
import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Function to scrape restaurant data from Google Maps
def scrape_google_maps_restaurants(location):
    options = Options()
    options.add_argument("--headless")  # Run in the background
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280,800")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open Google Maps and search for restaurants
    search_url = f"https://www.google.com/maps/search/restaurants+in+{location.replace(' ', '+')}/"
    driver.get(search_url)
    time.sleep(random.uniform(5, 8))  # Wait for results to load

    # Scroll to load more results
    for _ in range(5):  # Adjust number of scrolls as needed
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(random.uniform(2, 4))

    # Extract restaurant data
    restaurants = []
    results = driver.find_elements(By.CLASS_NAME, "Nv2PK")

    for result in results:
        try:
            name = result.find_element(By.CLASS_NAME, "qBF1Pd").text
            rating = result.find_element(By.CLASS_NAME, "MW4etd").text if result.find_elements(By.CLASS_NAME, "MW4etd") else "N/A"
            address = result.find_element(By.CLASS_NAME, "W4Efsd").text if result.find_elements(By.CLASS_NAME, "W4Efsd") else "N/A"
            restaurants.append([name, rating, address])
        except Exception as e:
            print(f"Error extracting data: {e}")

    driver.quit()

    # Save data to CSV
    df = pd.DataFrame(restaurants, columns=["Name", "Rating", "Phone Number", "Address"])
    data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    filename = os.path.join(data_folder, f"restaurants_{location.replace(' ', '_').lower()}.csv")
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"✅ Data saved to {filename}")

if __name__ == "__main__":
    location = input("Enter the location to scrape restaurants: ")
    scrape_google_maps_restaurants(location)