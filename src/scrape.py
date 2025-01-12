"""
This script scrapes product data from Best Buy for laptops and headphones using the Scraper_2000_best_buy_ed function.
It processes the scraped data by concatenating the results into Pandas DataFrames and then saves them as CSV files.
"""
from functions import Scraper_2000_best_buy_ed, save_dataframe_to_csv
import pandas as pd

# Define URLs for scraping laptop and headphone deals
url ='https://www.bestbuy.com/site/promo/laptop-and-computer-deals?cp=1&qp=category_facet%3Dname~pcmcat138500050001%5Ecurrentoffers_facet%3DCurrent%20Deals~On%20Sale&sp=-currentprice%20skuidsaas'
url2 = 'https://www.bestbuy.com/site/searchpage.jsp?_dyncharset=UTF-8&browsedCategory=pcmcat1720706915460&cp=1&id=pcat17071&iht=n&ks=960&list=y&qp=category_facet%3Dname~pcmcat144700050004%5Ecurrentoffers_facet%3DCurrent%20Deals~Clearance%5Epercentdiscount_facet%3DDiscount~All%20Discounted%20Items&sc=Global&sp=-currentprice%20skuidsaas&st=pcmcat1720706915460_categoryid%24abcat0204000&type=page&usc=All%20Categories'

# Scrape data for laptops and headphones
scraped_df_lists_laptops = Scraper_2000_best_buy_ed(url)
scraped_df_lists_headphones = Scraper_2000_best_buy_ed(url2)

# Concatenate the scraped data into single DataFrames
df_laptops = pd.concat(scraped_df_lists_laptops, ignore_index=True)
df_headphones = pd.concat(scraped_df_lists_headphones, ignore_index=True)

# Save the DataFrames to CSV files
save_dataframe_to_csv(df_laptops,"data/data_laptops.csv")
save_dataframe_to_csv(df_headphones, "data/data_headphones.csv")

