# Scraping dataframe of Captains active during (2000-2016) then sorting them by End_Date

import urllib

from bs4 import BeautifulSoup

url = "http://stats.espncricinfo.com/ci/content/records/283747.html"

page = urllib.urlopen(url)

soup = BeautifulSoup(page)

table = soup.find_all("tbody")

Captain = []
Span = []

cell = []
list = []

# make a list of captains and corresponding spans

for item in table:
    table2 = item.find_all('tr')

for item in table2:
    for i in range(0,8):
        cell.append(item.find_all('td')[i].text)
    list.append(cell)
    cell = []

for i in range(len(list)):
    Captain.append(list[i][0])
    Span.append(list[i][1])

Selected_Caps = []
Selected_Span = []

Countries = ['INDIA','PAK','SL','NZ','AUS','SA','WI','ZIM','BDESH']

for i in range(len(Span)):
    a,b = Span[i].split("-")
    for country in Countries:
        if (a>='2000' or (b <= '2016' and b > '2000')) and (country in Captain[i]):
            Selected_Caps.append(Captain[i])
            Selected_Span.append(Span[i])

block = []
lists = []

import numpy as np
# Sorting as per End Date

for i in range(len(Selected_Caps)):
    startDate, endDate = Selected_Span[i].split("-")
    block.append(Selected_Caps[i])
    block.append(endDate)
    block.append(Selected_Span[i])
    lists.append(block)
    block = []

sorted_list = sorted(lists,key=lambda x: x[1])

# Making DF
SortedCap = []
SortedSpan = []
for i in range(len(sorted_list)):
    SortedCap.append(sorted_list[i][0])
    SortedSpan.append(sorted_list[i][2])

import pandas as pd

df = pd.DataFrame()
df['Captain'] = SortedCap
df['Span'] = SortedSpan

df.to_csv('Captains.csv')