# review_scraper.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse

def init_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    return webdriver.Chrome(options=options)

def extract_platform_name(url):
    # 예: "https://www.oliveyoung.com/reviews?page=2" → "oliveyoung"
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    platform = domain.split('.')[0]  # "oliveyoung"
    return platform

def get_reviews_from_page(html, platform):
    soup = BeautifulSoup(html, "html.parser")
    reviews = []

    review_blocks = soup.find_all("div", class_="review")  # 예시 구조
    for block in review_blocks:
        product = block.find("div", class_="product-name").text.strip()
        review = block.find("p", class_="review-text").text.strip()
        reviews.append({
            "product_name": product,
            "review": review,
            "platform": platform
        })

    return reviews

def scrape_reviews(base_url, max_pages=5):
    driver = init_driver()
    all_reviews = []
    platform = extract_platform_name(base_url)

    for page in range(1, max_pages + 1):
        url = f"{base_url}?page={page}"
        driver.get(url)
        time.sleep(2)
        page_html = driver.page_source
        reviews = get_reviews_from_page(page_html, platform)
        all_reviews.extend(reviews)

    driver.quit()
    return pd.DataFrame(all_reviews)

if __name__ == "__main__":
    base_url = "https://www.oliveyoung.com/reviews"  # 대체 필요
    df = scrape_reviews(base_url, max_pages=3)
    df.to_csv("../data/scraped_reviews.csv", index=False)
    print("Saved scraped reviews.")
