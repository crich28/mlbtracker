
from importlib.resources import contents
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.espn.com/mlb/playerratings'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')
body = doc.find_all('table')

data =[]   
    
trs = body[2].find_all('tr')
for tr in trs[3:]:
    td = tr.find_all("td")
    for line in td[1:6]:
        line = line.string
        data.append(line)
    


    
def spliiter(list,n):
    for i in range(0,len(list),n):
        yield list[i:i+n]

stats = (list(spliiter(data,5)))

tags = ['Player', 'Team', 'Pos', 'Rank', 'Ratings']  
filename = 'mlbrankings.csv'      
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(tags)
    csvwriter.writerows(stats)
