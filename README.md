# Product Review ETL Pipeline

This project simulates a real-world ETL (Extract-Transform-Load) process for collecting, cleaning, matching, and storing product review data.  
It is based on my experience during a previous internship, reimplemented here for demonstration purposes.

---

## 🔄 Pipeline Overview

1. **Collect**:  
   - REST API (paginated GET requests with variable URL param)  
   - Selenium + BeautifulSoup fallback when API outdated

2. **Clean**:  
   - Deduplicate by exact match on review text  
   - Liberal filtering, minimal normalization

3. **Match**:  
   - Fuzzy matching + regex between scraped product names and internal reference list

4. **Store**:  
   - Store into MySQL using `pymysql`, with dynamic table naming (`table_name_YYYYMMDD`)

---

## 📁 Folder Structure

- `data/`  
  - `sample_reviews.csv`  
  - `product_reference.csv`

- `scripts/`  
  - `review_api_fetch.ipynb`  
  - `review_scraper.py`  
  - `review_cleaner.py`  
  - `product_matcher.py`  
  - `db_uploader.py`

---

## 🛠️ Tech Stack

- Python, Jupyter Notebook  
- Requests, Selenium, BeautifulSoup4  
- pandas, regex, RapidFuzz  
- pymysql

---

## ⚠️ Note

This is a simplified and anonymized reimplementation of an actual data flow.  
All code and data are self-created and do not reflect any proprietary materials.
