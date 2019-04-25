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
    try:
        codeProductFromPage = soup.find(class_="m-typo m-typo_secondary").text
        if(codeProduct in codeProductFromPage):
            PRICE = soup.find(class_="is-regular").text
            PRICE = PRICE.replace("zł", "")
            PRICE = PRICE.replace("PLN", "")
            PRICE = PRICE.strip()
            print("cena: " + PRICE+ "$#$#")
    except:
        o=1

codeProduct = str(sys.argv[1])
linkProduct = str(sys.argv[2])
tagfunc(codeProduct, linkProduct)