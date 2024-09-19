import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
# import re

url = "https://icanig.org/ican/students/professional/professional-learning-materials.php#profMaterials"
# code = re.compile(r"*SKILLS*.pdf")
folder_location = r"C:\webscrape"
if not os.path.exists(folder_location):
    os.mkdir(folder_location)

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
for link in soup.select(f"a[href$='.pdf']"):
    filename = os.path.join(folder_location, link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url, link['href'])))
