#!/usr/bin/python3

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?id=13880;type=tournament'
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find('table',{'class': 'engineTable'})
trs = table.find_all('tr')
print(trs)

rows = []
columns = ['Player','Mat','Inns','NO','Runs','HS','Ave','BF','SR','100','50','0','4s','6s']

for tr in trs[1:]:
    tds = tr.find_all('td')
    row = [td.text.replace('\n','').strip() for td in tds]
    rows.append(row)
df = pd.DataFrame(rows,columns=columns)
df.to_csv('most_runs.csv', index=False)


