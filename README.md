# Google Maps Restaurant Scraper

## 📌 Description

This Python script scrapes restaurant data from Google Maps for a given location using Selenium. It extracts restaurant names, ratings, and addresses, then saves the data in a CSV file.

### 🔹 Features
- ✅ No API key required
- ✅ Works with Google Maps search
- ✅ Bypasses Google CAPTCHA by avoiding direct search scraping
- ✅ Scrapes restaurant name, rating, and address
- ✅ Handles scrolling for more results
- ✅ Saves data as a CSV file

## 🛠 Requirements

Ensure you have the following installed:

- **Python 3.7+**
- **Google Chrome (latest version)**
- **Chrome WebDriver** (automatically managed by `webdriver-manager`)

### Install Required Python Libraries:
```bash
pip install selenium pandas webdriver-manager
```

## 🚀 Installation & Usage

### Clone the Repository:
```bash
git clone https://github.com/yourusername/google-maps-scraper.git
cd google-maps-scraper
```

### Install Dependencies:
```bash
pip install -r requirements.txt
```

### Run the Script:
```bash
python scrape_restaurants.py
```

Enter a location when prompted (e.g., "Koramangala, Bengaluru").

### 📂 Find Your Data:
The scraped data will be saved in the `data/` folder as a CSV file:
```bash
data/restaurants_koramangala.csv
```

## ⚠️ Notes

- Running in **headless mode** to avoid UI popups.
- Ensure **Google Chrome is up to date**.
- **May need manual intervention** if Google updates its structure.

## 📜 License

This project is licensed under the **MIT License**.

## 🤝 Contributing

Pull requests are welcome! If you find any bugs or want to add features, feel free to fork the repository and submit a PR.
