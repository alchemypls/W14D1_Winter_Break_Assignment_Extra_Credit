# BestBuy Scraper & Analysis

This project scrapes product data from Best Buy for laptops and headphones, processes the data with Pandas, and visualizes key metrics using Matplotlib and Seaborn.

## Overview

- **Scraping:**  
  Uses web scraping functions to extract product details such as prices, discount percentages, and saved amounts from Best Buy pages spread across multiple pages.

- **Data Processing:**  
  Combines and cleans the scraped data, calculating average and total cash savings, as well as discount percentages.

- **Visualization:**  
  Creates bar plots to display average and total cash amounts for laptops and headphones.

## Requirements

- Python 3.x
- Pandas
- Requests
- BeautifulSoup4
- Matplotlib
- Seaborn
- NumPy

## Usage

1. **Scrape Data:**  
   Run the scraper script to extract and save product data into CSV files.

   ```bash
   python scraper_script.py
2. **Analyze & Visualize:**
Run the analysis script to generate visualizations.

```bash
python analysis_script.py
```
3. **Files**

functions.py: Contains the web scraping functions.

scrape.py: Script that scrapes data and saves CSV files.

plots.py: Script that reads CSV files, processes the data, and visualizes the results.
