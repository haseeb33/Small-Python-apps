# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 22:01:57 2017

@author: Haseeb Bhai
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content

page_nbr = soup.find_all("a", {"class": "Page"})[-1].text
soup = BeautifulSoup(c, "html.parser")

allData = []
for i in range(0, int(page_nbr)*10, 10):
    print("http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="+str(i)+".html")
    allDiv = soup.find_all("div", {"class": "propertyRow"})
        
    for i in allDiv:
        d = {}
        d["Price"] = i.find("h4", {"class": "propPrice"}).text.replace("\n" , "").replace(" " , "")
        d["Address"] = i.find_all("span", {"class": "propAddressCollapse"})[0].text
        d["Locality"] = i.find_all("span", {"class": "propAddressCollapse"})[1].text
        try:
            d["Beds"] = i.find("span", {"class": "infoBed"}).find("b").text
        except:
            d["Beds"] = None
        try:
            d["Area"] = i.find("span", {"class": "infoSqFt"}).find("b").text
        except:
            d["Area"] = None
        try:
            d["Full Baths"] = i.find("span", {"class": "infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"] = None
        try:
            d["Half Baths"] = i.find("span", {"class": "infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"] = None
        
        for column_group in i.find_all("div", {"class": "columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span", {"class": "featureGroup"}), column_group.find_all("span", {"class": "featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text
        allData.append(d)
        
df = pd.DataFrame(allData)
df.to_csv("Output.csv")