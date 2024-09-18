import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.scrapingcourse.com/ecommerce/")
soup = BeautifulSoup(response.content, "html.parser")
link_elements = soup.select("a[href]")

urls = []
for link_element in link_elements:
    url = link_element['href']
    if "https://www.scrapingcourse.com/ecommerce/" in url:
        urls.append(url)


urls = ["https://www.scrapingcourse.com/ecommerce/"]



