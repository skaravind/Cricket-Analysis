# Scraping innings and getting win and loss data of each inning in the span of

Team = []
Result = []
RPO = []
Opponent = []
Date = []

import urllib
from bs4 import BeautifulSoup

for x in range(1,73):
    URL = "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;filter=advanced;orderby=start;page="+str(x)+";spanmax1=31+Dec+2016;spanmin1=01+Jan+2000;spanval1=span;team=2;team=25;team=3;team=4;team=5;team=6;team=7;team=8;team=9;template=results;type=team;view=innings"
    page = urllib.urlopen(URL)
    soup = BeautifulSoup(page)
    table = soup.find_all('tbody')

    for item in table:
        row = item.find_all('tr')

    col = []

    for i in row:
        for j in range(len(i.find_all('td'))):
            col.append(i.find_all('td')[j].text)
        Team.append(col[0])
        Result.append(col[5])
        Opponent.append(col[7])
        Date.append(col[9])
        RPO.append(col[3])
        col = []

import pandas as pd

df = pd.DataFrame()

df['Team'] = Team
df['Opponent'] = Opponent
df['Result'] = Result
df['RPO'] = RPO
df['Date'] = Date

df.to_csv('Matches.csv')