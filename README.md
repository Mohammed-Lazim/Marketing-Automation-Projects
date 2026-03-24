# Marketing Automation & Technical SEO Suite 🚀
This repository contains a collection of Python-based tools designed to automate repetitive digital marketing tasks, perform competitor intelligence, and scale SEO operations.

## 🛠 Project 3: Professional SEO Automation Tool
**File:** `search_automation.py`

### Overview
A robust Selenium-based automation script that performs localized keyword searches and captures visual evidence of search engine results (SERPs). 

### Key Features
*   **Multi-Browser Support:** Automatically detects and launches available browsers (Chrome, Edge, or Brave).
*   **Stealth Mode:** Implements `undetected_chromedriver` and human-like typing delays to bypass basic bot detection.
*   **Automated Reporting:** Generates a timestamped screenshot of search results for audit and client reporting.
*   **Professional Logic:** Includes error handling for missing drivers and browser binaries.

### How to Run
1. Ensure you have Chrome/, Edge, or Brave installed.
2. Install dependencies: `pip install selenium webdriver-manager undetected-chromedriver`
3. Run: `python search_automation.py`
4. Enter your target keyword when prompted.

---

## 🛠 Project 2: Competitor Intelligence Scraper
**File:** `competitor_seo_scraper.py`

### Overview
A web-scraping utility built with BeautifulSoup to extract content data from target URLs for SEO gap analysis.

### Key Features
*   **Data Extraction:** Pulls titles and authors/categories into a structured format.
*   **Export Function:** Automatically generates a `competitor_analysis.csv` for use in Excel or Google Sheets.

---

## 🛠 Project 1: Ad Performance ROI Analyzer
**File:** `ad_performance_analyzer.py`

### Overview
A data analytics script using the **Pandas** library to process messy marketing spend reports.

### Key Features
*   **Metric Calculation:** Automatically calculates ROAS (Return on Ad Spend) and CPC (Cost Per Click).
*   **Profitability Filter:** Segregates high-performing ads from budget-wasting campaigns.
