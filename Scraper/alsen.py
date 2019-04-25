# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, sys
				
def tagfunc(codeProduct):
    global PRICE
    splitter = ("$#$#")
    codeProduct = codeProduct.replace(splitter, " ")
    codeProductSearch = codeProduct.replace(" ", "+") 
    lengthCode = len(codeProduct)   
    listPrices = []
    listLinks = []
    
    page = requests.get("http://www.alsen.pl/search?query%5Bmenu_item%5D=&query%5Bquerystring%5D=" + codeProductSearch)
    soup = BeautifulSoup(page.content, 'lxml')
    pclab = soup.find_all(class_="m-productItem_headline")
    for i in pclab:
        LINK =  "http://www.alsen.pl" + i.a['href']	
        tmp = requests.get(LINK)
        soup2 = BeautifulSoup(tmp.content, 'lxml')
         
        codeProductFromPage = soup2.find(class_="s-productNrs clearfix").text
        temp, codeProductFromPage = codeProductFromPage.split("Kod producenta: ")
        PRICE = soup2.find(class_="m-productItem_price").text
        PRICE = PRICE.replace("zł", "")
        PRICE = PRICE.strip()
        if(codeProduct in codeProductFromPage):
            listPrices.append(PRICE)
            listLinks.append(LINK)
    
    prices = ""
    links = ""
    for x in range(0, len(listLinks)):
        prices = prices + listPrices[x] + "$#$#"
        links = links + listLinks[x] + "$#$#"
    print("link: "+ links + "&&&" + "cena: " + prices)

cProduct = str(sys.argv[1])
tagfunc(cProduct)