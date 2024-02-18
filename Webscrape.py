import requests

from bs4 import BeautifulSoup
import pandas as pd
import time

#Getting the politician IDs e.g., Debbie Dingell D000624
url = "https://www.capitoltrades.com/politicians?per_page=96&txDate=365d"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

politician_ids = []
for row in soup.select('tbody.lister-list tr'):
    politician_id = row.find(q-widget q-index-card polician-index-card entity -- politician id('td', class_='q-widget-body index-card-body politician-index-card-body').find('span', class_='q-cell cell--name').find('a').gettext()

print (politician_id)

time.sleep(1)