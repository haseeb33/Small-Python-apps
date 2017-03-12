# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 22:01:57 2017

@author: Haseeb Bhai
"""

import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content

soup = BeautifulSoup(c, "html.parser")

allDiv = soup.find_all("div", {"class": "propertyRow"})


for i in allDiv:
    print(i.find("h4", {"class": "propPrice"}).text.replace("\n" , "").replace(" " , ""))
    print(i.find_all("span", {"class": "propAddressCollapse"})[0].text)
    print(i.find_all("span", {"class": "propAddressCollapse"})[1].text)
    try:
        print(i.find("span", {"class": "infoBed"}).find("b").text)
    except:
        print(None)
    try:
        print(i.find("span", {"class": "infoSqFt"}).find("b").text)
    except:
        print(None)
    try:
        print(i.find("span", {"class": "infoValueFullBath"}).find("b").text)
    except:
        print(None)
    try:
        print(i.find("span", {"class": "infoValueHalfBath"}).find("b").text)
    except:
        print(None)
    
    for column_group in i.find_all("div", {"class": "columnGroup"}):
        for feature_group, feature_name in zip(column_group.find_all("span", {"class": "featureGroup"}), column_group.find_all("span", {"class": "featureName"})):
            if "Lot Size" in feature_group.text:
                print(feature_name.text)
    print(" ")
    
#print(i.find())


#print(allPrices)









