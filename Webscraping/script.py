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

print(soup.prettify())