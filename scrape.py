from datetime import timedelta, date
import requests
from bs4 import BeautifulSoup
import boto3

url = 'https://www.basketball-reference.com/teams/CHI/1997.html'
r = requests.get(url)
html = r.content
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

dynamoDB = boto3.client('dynamodb', region_name='us-west-2',
                        endpoint_url='http://localhost:8000')

for row in table_rows:
    player_row = row.find('td')
    playernum = row.find('th')
    player_number = playernum.text
    player = player_row.find('a')
    player_name = player.text
    print(
        f'This players name is {player.text} Jersey number: {player_number}')

    dynamoDB.put_item(
        TableName="Player",
        Item={
            "PlayerName": {"S": player_name},
            "PlayerNumber": {"N": player_number},
        }
    )
#


# print(html)
