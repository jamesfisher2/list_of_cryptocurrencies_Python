import json
from bs4 import BeautifulSoup
import requests

### Fetching all cyrpto symbols via API ###

url = "https://min-api.cryptocompare.com/data/all/coinlist"
response = requests.get(url)

# First version
# soup = BeautifulSoup(response.content, "html.parser")
# data = json.loads(soup.prettify())

# Second version
data = json.loads(response.content)

data = data['Data']

print("General information for debugging purposes")
print(type(data))           #<class 'dict'>
print(len(data.keys()))     #8344

print("\nList of all cryptos:")
print(data.keys())

print("\nList of sorted cryptos:")
crypto_lst = sorted(list(data.keys()))
print(crypto_lst)


### Fetching cyrptos via API sorted by market capitalization ###

ccy = "USD"
topN = 10

#url2 = "https://min-api.cryptocompare.com/data/top/mktcapfull?limit=10&tsym=USD"       #original REST
url2 = "https://min-api.cryptocompare.com/data/top/mktcapfull?limit=" + str(topN) + "&tsym=" + ccy
response2 = requests.get(url2)

# First version
# soup2 = BeautifulSoup(response2.content, "html.parser")
# dic = json.loads(soup2.prettify())

# Second version
dic = json.loads(response2.content)

data2 = dic['Data']

#for debugging purposes
# an individual data cell
data2[0].keys       # dict_keys(['CoinInfo', 'RAW', 'DISPLAY'])
data2[0]['RAW']     # cyrptocurrency ranked as #1 (RAW data)



print("\nTop cryptos by market capitalizaion in miliards of $:")
coin_lst_mcap = []
for i in range(len(data2)):
    try:
        #coin_lst_mcap.extend([[i, data2[i]['RAW'][ccy]['FROMSYMBOL'], round(data2[i]['RAW'][ccy]['MKTCAP'])]])
        coin_lst_mcap.extend([[i, data2[i]['RAW'][ccy]['FROMSYMBOL'], round(data2[i]['RAW'][ccy]['MKTCAP'] / 1000000000, 2)]])      #rounding to miliards $
    except:
        pass

print(coin_lst_mcap)