# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, sys
from decimal import Decimal

def tagfunc(codeProduct, nProduct):
    global PRICE
    splitter = ("$#$#")
    codeProduct = codeProduct.replace(splitter, " ")
    codeProductSearch = codeProduct.replace(" ", "+") 
    lengthCode = len(codeProduct)   
    listPrices = []
    listLinks = []
    try:
        page = requests.get("https://www.ceneo.pl/;szukaj-" + codeProductSearch)
        soup = BeautifulSoup(page.content, 'lxml')
        mainPages = soup.find_all(class_="cat-prod-row-name")
        for i in mainPages:
            productNameFromPage = i.text
            if(nProduct in productNameFromPage):
                LINK = "https://www.ceneo.pl" + i.a['href']
                productQuantity = 0
                PRICE = 0
                tmp = requests.get(LINK)
                soup2 = BeautifulSoup(tmp.content, 'lxml')
            
                products = soup2.find_all(class_="product-offer js_product-offer")
                for j in products:
                    priceTemp =j.find('span', class_="price").text
                    productQuantity = productQuantity + 1
                    PRICE += Decimal(priceTemp.replace(",", "."))

                PRICE = round(PRICE / productQuantity, 2)
                listPrices.append(str(PRICE).replace(".", ","))
                listLinks.append(LINK)
                
            else:
                continue
    except:
            a = 2
    prices = ""
    links = ""
    for x in range(0, len(listLinks)):
        prices = prices + listPrices[x] + "$#$#"
        links = links + listLinks[x] + "$#$#"
    print("link: "+ links + "&&&" + "cena: " + prices)

cProduct = str(sys.argv[1])
nProduct = str(sys.argv[2])
tagfunc(cProduct, nProduct)