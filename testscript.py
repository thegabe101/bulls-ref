from datetime import timedelta, date
import requests
from bs4 import BeautifulSoup
import boto3


url = 'https://www.basketball-reference.com/teams/CHI/1997.html'
r = requests.get(url)
html = r.content
id = ''
soup = BeautifulSoup(html, 'html.parser')
div = soup.find(id='all_roster')
rawHtml = soup.find('html')

for table in soup.find_all('table'):
    if table.get('id') == 'roster':
        player_table = table
        print(player_table)


tbody = player_table.find('tbody')
table_rows = tbody.find_all('tr')
print(f"found {len(table_rows)} players ")

for row in table_rows:
    print(row)


# print(html)
