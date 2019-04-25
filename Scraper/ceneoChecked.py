# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, sys
from decimal import Decimal

def tagfunc(nameProduct, linkProduct):
    global PRICE  
    listPrices = []
    try:
        page = requests.get(linkProduct)
        soup = BeautifulSoup(page.content, 'lxml')
        
        products = soup.find_all(class_="product-offer js_product-offer")
        for j in products:
            priceTemp =j.find('span', class_="price").text
            listPrices.append(Decimal(priceTemp.replace(",", ".")))
     
    except:
            a = 2
    
    print("cena: " + str(min(listPrices)).replace(".", ",") + "$#$#")

nameProduct = str(sys.argv[1])
linkProduct = str(sys.argv[2])
tagfunc(nameProduct, linkProduct)
