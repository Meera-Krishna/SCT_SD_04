from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

search_term = input("🔍 Enter Myntra product search term (e.g., tops for women): ").strip().replace(" ", "%20")
base_url = "https://www.myntra.com"
max_pages = 5  # ⏭️ Adjust this to scrape more pages

# 🔧 Chrome setup (non-headless recommended for debugging)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 📂 CSV setup
csv_filename = f"{search_term.replace('%20', '_')}_myntra_products.csv"
with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Original Price", "Discounted Price", "Rating", "Product URL", "Image URL"])

    for page in range(1, max_pages + 1):
        url = f"https://www.myntra.com/{search_term}?p={page}"
        print(f"🔄 Scraping page {page}: {url}")
        driver.get(url)
        time.sleep(5)

        products = driver.find_elements(By.XPATH, '//li[contains(@class,"product-base")]')

        if not products:
            print("❌ No products found. Stopping.")
            break

        for product in products:
            try:
                brand = product.find_element(By.CLASS_NAME, "product-brand").text
                title = product.find_element(By.CLASS_NAME, "product-product").text
                name = f"{brand} {title}"
            except:
                name = "N/A"

            try:
                discounted_price = product.find_element(By.CLASS_NAME, "product-discountedPrice").text
            except:
                discounted_price = "N/A"

            try:
                original_price = product.find_element(By.CLASS_NAME, "product-strike").text
            except:
                try:
                    original_price = product.find_element(By.CLASS_NAME, "product-price").text
                except:
                    original_price = "N/A"

            try:
                rating = product.find_element(By.CLASS_NAME, "product-ratingsContainer").text
            except:
                rating = "N/A"

            try:
                product_url = product.find_element(By.TAG_NAME, "a").get_attribute("href")
            except:
                product_url = "N/A"

            try:
                image_url = product.find_element(By.TAG_NAME, "img").get_attribute("src")
            except:
                image_url = "N/A"

            writer.writerow([name, original_price, discounted_price, rating, product_url, image_url])

        print(f"✅ Page {page} scraped.")

driver.quit()
print(f"\n✅ Scraping complete. Data saved to '{csv_filename}'")
