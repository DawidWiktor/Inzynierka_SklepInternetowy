# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, sys
				
def tagfunc(codeProduct, linkProduct):
    global PRICE
    splitter = ("$#$#")
    codeProduct = codeProduct.replace(splitter, " ")
    codeProductSearch = codeProduct.replace(" ", "_") 
    lengthCode = len(codeProduct)   
    page = requests.get(linkProduct)
    soup = BeautifulSoup(page.content, 'lxml')
    codeProductFromPage = soup.find(itemprop="mpn").text
    if(codeProduct in codeProductFromPage):
        PRICE = soup.find(class_="pull-right price").text
        PRICE = PRICE.replace("zł", "")
        PRICE = PRICE.strip()   
    print("cena: " + PRICE + "$#$#")


codeProduct = str(sys.argv[1])
linkProduct = str(sys.argv[2])
tagfunc(codeProduct, linkProduct)