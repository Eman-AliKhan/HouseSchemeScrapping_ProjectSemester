from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# === Setup Chrome WebDriver ===
# Replace this with your own path to chromedriver
chromedriver_path = r"C:\WebDriver\chromedriver.exe"  # Windows example

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Start Chrome driver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# === Open the PSX DPS portal ===
url = "https://dps.psx.com.pk"
driver.get(url)

# Wait for JavaScript content to load
time.sleep(5)  # increase if your net is slow

# === Scrape visible data (e.g., card titles or sections) ===
# You can change tags based on what you want (e.g., table rows, headings, etc.)
print("Scraped Headings or Cards:\n")

elements = driver.find_elements(By.TAG_NAME, "h5")  # Example: all h5 headings
for el in elements:
    text = el.text.strip()
    if text:
        print("-", text)

# === Optional: Scrape paragraphs or table entries ===
print("\nScraped Paragraphs:\n")
paragraphs = driver.find_elements(By.TAG_NAME, "p")
for p in paragraphs:
    text = p.text.strip()
    if text:
        print("-", text)

# === Finish up ===
driver.quit()
