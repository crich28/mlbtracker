import csv
from fileinput import filename
from tokenize import Name
import requests
from bs4 import BeautifulSoup


url = 'https://www.espn.com/mlb/playerratings'
result = requests.get(url)
doc = BeautifulSoup(result.text, 'html.parser')
body = doc.find_all('td')



data =[]
for td in body[13:]:
    for tag in td.contents[1:6]:
        strings=tag.string
        data.append(strings)


def splitter(list, n):
    for i in range(0,len(list),n):
        yield list[i:i+n]     

stats = list(splitter(data,5))

tags = ['Player', 'Team', 'Pos', 'Rank', 'Ratings']  
filename = 'mlbrankings.csv'      
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(tags)
    csvwriter.writerows(stats)
