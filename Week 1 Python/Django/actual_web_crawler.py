import requests
from bs4 import BeautifulSoup
import csv

urls = ["https://www.scrapingcourse.com/ecommerce/"]
products = []
touched = 0
worked = 0
while len(urls) != 0:
    current_url = urls.pop()
    response = requests.get(current_url)
    soup = BeautifulSoup(response.content, "html.parser")
    link_elements = soup.select("a[href]")
    for link_element in link_elements:
        url = link_element['href']
        if "https://www.scrapingcourse.com/ecommerce/" in url:
            urls.append(url)
            product = {}
            product["url"] = current_url
            try:
                product["image"] = soup.select_one(".wp-post-image")["src"]
                product["title"] = soup.select_one(".product_title").text()
                product["price"] = soup.select_one(".price")
                products.append(product)
                worked = worked + 1
            except TypeError:
                touched = touched + 1
                continue
            
print(f"{worked} urls were crawled though and we found no info on {touched} urls.")
with open('products.csv', "w") as csv_file:
    writer = csv.writer(csv_file)
    for product in products:
        writer.writerow(product.values())

print("I am done")