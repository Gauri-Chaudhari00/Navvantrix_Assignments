# -*- coding: utf-8 -*-
"""Web Scraping for Product Details.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AhhChPStnNMZlq3ftw9OIa_9u-wqYsXl
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# Function to extract Product Title
def get_title(soup):

    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})

        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

# Function to extract Product Price
def get_price(soup):

    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()

    except AttributeError:

        try:
            # If there is some deal price
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()

        except:
            price = ""

    return price

# Function to extract Product Rating
def get_rating(soup):

    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()

    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""

    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = ""

    return review_count

# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available = available.find("span").string.strip()

    except AttributeError:
        available = "Not Available"

    return available

if __name__ == '__main__':

    # add your user agent
    HEADERS = ({'User-Agent':'', 'Accept-Language': 'en-US, en;q=0.5'})

    # The webpage URL
    URL = "https://www.amazon.com/s?k=playstation+4&ref=nb_sb_noss_2"

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

    # Store the links
    links_list = []

    # Loop for extracting links from Tag Objects
    for link in links:
            links_list.append(link.get('href'))

    d = {"title":[], "price":[], "rating":[], "reviews":[],"availability":[]}

    # Loop for extracting product details from each link
    for link in links_list:
        new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)

        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        # Function calls to display all necessary product information
        d['title'].append(get_title(new_soup))
        d['price'].append(get_price(new_soup))
        d['rating'].append(get_rating(new_soup))
        d['reviews'].append(get_review_count(new_soup))
        d['availability'].append(get_availability(new_soup))


    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df['title'].replace('', np.nan, inplace=True)
    amazon_df = amazon_df.dropna(subset=['title'])
    amazon_df.to_csv("amazon_data.csv", header=True, index=False)

amazon_df

from google.colab import sheets
sheet = sheets.InteractiveSheet(df=amazon_df)

#flipkart

# Function to extract Product Title
def get_title(soup):
    try:
        title = soup.find("span", attrs={"class": "B_NuCI"})
        title_value = title.text
        title_string = title_value.strip()
    except AttributeError:
        title_string = ""
    return title_string

# Function to extract Product Price
def get_price(soup):
    try:
        price = soup.find("div", attrs={'class': '_30jeq3'}).string.strip()
    except AttributeError:
        price = ""
    return price

# Function to extract Product Rating
def get_rating(soup):
    try:
        rating = soup.find("div", attrs={'class': '_3LWZlK'}).string.strip()
    except AttributeError:
        rating = ""
    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'class': '_2_R_DZ'}).text.strip()
    except AttributeError:
        review_count = ""
    return review_count

# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'class': '_16FRp0'})
        available = available.text.strip()
    except AttributeError:
        available = "Not Available"
    return available

if __name__ == '__main__':
    # Add your user agent
    HEADERS = ({'User-Agent':'Mozilla/5.0', 'Accept-Language': 'en-US, en;q=0.5'})

    # The webpage URL
    URL = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Fetch links as List of Tag Objects
    links = soup.find_all("a", attrs={'class': 'IRpwTa'})

    # Store the links
    links_list = []

    # Loop for extracting links from Tag Objects
    for link in links:
        links_list.append(link.get('href'))

    d = {"title": [], "price": [], "rating": [], "reviews": [], "availability": []}

    # Loop for extracting product details from each link
    for link in links_list:
        new_webpage = requests.get("https://www.flipkart.com" + link, headers=HEADERS)
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        # Function calls to display all necessary product information
        d['title'].append(get_title(new_soup))
        d['price'].append(get_price(new_soup))
        d['rating'].append(get_rating(new_soup))
        d['reviews'].append(get_review_count(new_soup))
        d['availability'].append(get_availability(new_soup))

    # Create a DataFrame and save to CSV
    flipkart_df = pd.DataFrame.from_dict(d)
    flipkart_df['title'].replace('', np.nan, inplace=True)
    flipkart_df = flipkart_df.dropna(subset=['title'])
    flipkart_df.to_csv("flipkart_data.csv", header=True, index=False)

    flipkart_df

flipkart_df

from google.colab import sheets
sheet = sheets.InteractiveSheet(df=flipkart_df)