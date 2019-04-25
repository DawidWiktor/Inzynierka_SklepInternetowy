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
    
    page = requests.get("https://vobis.pl/search?query%5Bquerystring%5D=" + codeProductSearch)
    soup = BeautifulSoup(page.content, 'lxml')
    try:
        codeProductFromPage = soup.find(class_="m-typo m-typo_secondary").text
        
        if(codeProduct in codeProductFromPage):
            PRICE = soup.find(class_="is-regular").text
            PRICE = PRICE.replace("zł", "")
            PRICE = PRICE.replace("PLN", "")
            PRICE = PRICE.replace("\n", "")
            PRICE = PRICE.strip()
            LINK = "https://vobis.pl" + soup.find(rel='canonical')['href']
            print("link: " + LINK + "$#$#"+ "&&&" + "cena: " + PRICE+ "$#$#")
    except:
        o=1

cProduct = str(sys.argv[1])
tagfunc(cProduct)