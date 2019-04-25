# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, sys
				
def tagfunc(codeProduct, linkProduct):
    global PRICE
    splitter = ("$#$#")
    codeProduct = codeProduct.replace(splitter, " ")
    codeProductSearch = codeProduct.replace(" ", "+") 
    lengthCode = len(codeProduct)   
    
    page = requests.get(linkProduct)
    soup = BeautifulSoup(page.content, 'lxml')
    codeProductFromPage = soup.find(class_="s-productNrs clearfix").text
    temp, codeProductFromPage = codeProductFromPage.split("Kod producenta: ")
    if(codeProduct in codeProductFromPage):
        PRICE = soup.find(class_="m-productItem_price").text
        PRICE = PRICE.replace("zł", "")
        PRICE = PRICE.strip()       

    print("cena: " + PRICE +"$#$#")

codeProduct = str(sys.argv[1])
linkProduct = str(sys.argv[2])
tagfunc(codeProduct, linkProduct)