from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

def save_dataframe_to_csv(df, filename):
    """
    Saves a Pandas DataFrame to a CSV file.

    Parameters:
        df (pd.DataFrame): The DataFrame to save.
        filename (str): The path to the CSV file.
    """
    try:
        df.to_csv(filename, mode='x')
    except:
        raise ValueError("DataFrame not valid")

def update_url_page(url, page_count=1):
    """
    Updates the page count parameter in the given URL.

    Parameters:
        url (str): The original URL containing the 'cp=' parameter.
        page_count (int): The desired page number to update in the URL.

    Returns:
        str: The updated URL with the new page count.
    """
    listed_url = url.split("cp=")
    updated_url = listed_url[0] + f"cp={page_count}" + listed_url[1][1:]
    return updated_url

def extract_source(url):
    """
    Fetches and parses the HTML content from a given URL.

    Parameters:
        url (str): The URL to send the HTTP GET request to.

    Returns:
        BeautifulSoup: A BeautifulSoup object containing the parsed HTML.
    """
    agent = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=agent)
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    return soup

def extract_data(soup):
    """
    Extracts and cleans product data from the BeautifulSoup object.

    Parameters:
        soup (BeautifulSoup): The parsed HTML content.

    Returns:
        pd.DataFrame: A DataFrame containing the cleaned product data.
    """
    raw_price = soup.find_all('div', class_="priceView-hero-price priceView-customer-price")
    raw_before_price = soup.find_all('div', class_="pricing-price__regular-price sr-only")
    raw_stats = soup.find_all('h4', class_='sku-title')
    root = 'https://www.bestbuy.com'

    cleaned_prices = [
        float(x.text.split()[-1].strip("$").replace(',', ""))
        for x in raw_price
    ]
    cleaned_before_price = [
        float(x.text.split()[-1].strip("$").replace(',', ""))
        for x in raw_before_price
    ]

    discount_percentage = [
        round(((original - discounted) / original) * 100)
        for original, discounted in zip(cleaned_before_price, cleaned_prices)
    ]
    saved_amount = [
        original - discounted
        for original, discounted in zip(cleaned_before_price, cleaned_prices)
    ]

    cleaned_stats = [re.split('-|–|—', x.text.strip()) for x in raw_stats]
    cleaned_names = [parts[0] + parts[1] for parts in cleaned_stats]
    cleaned_url = [root + x.a['href'] for x in raw_stats]

    default_columns = ["Product Name", "Price", "Discount Percentage", "Saved Amount", "URL"]
    data_zip = [
        [name, price, discount, saved, url]
        for name, price, discount, saved, url in zip(
            cleaned_names, cleaned_prices, discount_percentage, saved_amount, cleaned_url
        )
    ]
    hachi_roku = pd.DataFrame(data_zip, columns=default_columns)
    return hachi_roku

def Scraper_2000_best_buy_ed(url):
    """
    Scrapes product data from Best Buy by iterating through paginated results.

    Parameters:
        url (str): The base URL to start scraping from.

    Returns:
        list: A list of DataFrames containing product data from each page.
    """
    page_count = 0
    bool_check = True
    raw_df_data = []

    while bool_check:
        page_count += 1
        updated_url = update_url_page(url, page_count)
        extract_url = extract_source(updated_url)
        url_end = extract_url.body.find('h3', class_="no-results-message-new")
         
        if url_end:
            print("Done")
            bool_check = False
        else:
            print(f"Page Count: {page_count}")
            raw_df_data.append(extract_data(extract_url))
    return raw_df_data

    

