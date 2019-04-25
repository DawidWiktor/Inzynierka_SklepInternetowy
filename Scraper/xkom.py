# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, sys
				
def tagfunc(codeProduct):
    global PRICE
    splitter = ("$#$#")
    codeProduct = codeProduct.replace(splitter, " ")
    codeProductSearch = codeProduct.replace(" ", "_") 
    lengthCode = len(codeProduct)   
    listPrices = []
    listLinks = []
    
    page = requests.get("https://www.x-kom.pl/szukaj?q=" + codeProductSearch)
    soup = BeautifulSoup(page.content, 'lxml')
    pclab = soup.find_all(class_="product-item product-impression")
    for i in pclab:
        try:
            LINK =  "https://www.x-kom.pl" + i.a['href']
            tmp = requests.get(LINK)
            soup2 = BeautifulSoup(tmp.content, 'lxml')
         
            codeProductFromPage = soup2.find(itemprop="mpn").text
            PRICE = soup2.find(class_="pull-right price").text
            PRICE = PRICE.replace("zł", "")
            PRICE = PRICE.strip()
            if(codeProduct in codeProductFromPage):
                listPrices.append(PRICE)
                listLinks.append(LINK)

        except:
            continue

    prices = ""
    links = ""
    for x in range(0, len(listLinks)):
        prices = prices + listPrices[x] + "$#$#"
        links = links + listLinks[x] + "$#$#"
    print("link: "+ links + "&&&" + "cena: " + prices)


cProduct = str(sys.argv[1])
tagfunc(cProduct)