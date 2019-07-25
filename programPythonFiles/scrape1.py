# scrape1.py

# This python file will aim to programmatically
# access ApplicationXtender's web page in order
# to automatically upload info from CSV file made
# in SW-OCR python file.

import requests
from bs4 import BeautifulSoup
import urllib3

url = "http://axweb.southwire.com/wx/Main.aspx?DataSource=AX-Oracle"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup)