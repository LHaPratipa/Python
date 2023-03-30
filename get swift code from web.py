import pandas as pd
import bs4
import requests
import openpyxl

url = 'https://www.theswiftcodes.com/lithuania/' #Edit Link
pantipDict={} #สร้าง Dict เปล่าๆ
page = 1
k=0
for page in range(1,4): # Edit last page+1
  if page == 1:
    data = requests.get(url)
  else:
    data = requests.get(url + 'page/' + str(page) + '/')
  soup = bs4.BeautifulSoup(data.text)
  print(page, data)
  for i in range(0,len(soup.body.find_all('td', attrs={'class':'table-id'}))):
    tempDict={} #สร้าง dict ชั่วคราว
    tempDict['ID'] = soup.body.find_all('td', attrs={'class':'table-id'})[i].text
    tempDict['Bank'] = soup.body.find_all('td', attrs={'class':'table-name'})[i].text
    tempDict['City'] = soup.body.find_all('td', attrs={'class':'table-city'})[i].text
    tempDict['Branch'] = soup.body.find_all('td', attrs={'class':'table-branch'})[i].text
    tempDict['SWIFT Code'] = soup.body.find_all('td', attrs={'class':'table-swift'})[i].text
    tempDict['Country'] = soup.body.find_all('h2', attrs={'class':'headline'})[0].text.replace('Find ','').replace(' Bank SWIFT Codes','')
    pantipDict[k]=tempDict
    k=k+1

import pandas as pd
pantipDF=pd.DataFrame.from_dict(pantipDict, orient='index')
pantipDF
pantipDF.to_excel("output.xlsx",sheet_name='1', index=False) 