
import requests
from bs4 import BeautifulSoup


url = 'https://www.espn.com/mlb/playerratings'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')
body = doc.find_all('td')

for tr in body:
    for td in tr.contents[1:6]:
        print(td.string)
        print()
    

print()