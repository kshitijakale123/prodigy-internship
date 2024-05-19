import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the e-commerce website (Books to Scrape in this case)
url = "http://books.toscrape.com/"

# Send a GET request to the website
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all products on the page
products = soup.find_all('article', class_='product_pod')

# Lists to store the product information
product_names = []
product_prices = []
product_ratings = []

# Extract information for each product
for product in products:
    # Product name
    name = product.h3.a['title']
    product_names.append(name)
    
    # Product price
    price = product.find('p', class_='price_color').text
    product_prices.append(price)
    
    # Product rating
    rating = product.p['class'][1]
    product_ratings.append(rating)

# Create a DataFrame using pandas
data = {
    'Name': product_names,
    'Price': product_prices,
    'Rating': product_ratings
}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('products.csv', index=False)

print("Data has been successfully scraped and saved to products.csv")
