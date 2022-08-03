

import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.espn.com/mlb/playerratings'
result = requests.get(url)
body = BeautifulSoup(result.text, 'html.parser')
tables = body.find_all('table')

data =[]   
    
trs = tables[2].find_all('tr')
for tr in trs[3:]:
    tds = tr.find_all("td")
    row = []
    for td in tds[1:6]:
        td = td.string
        row.append(td)
    data.append(row)
    


    


tags = ['Player', 'Team', 'Pos', 'Rank', 'Ratings']  
filename = 'mlbrankings.csv'      
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(tags)
    csvwriter.writerows(data)
