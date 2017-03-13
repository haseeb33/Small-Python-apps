# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:47:33 2017

@author: Haseeb Bhai
"""

from pandas_datareader import data
import datetime as dt

start = dt.datetime(2016, 8, 1)
end = dt.datetime(2016, 9, 16)

df = data.DataReader(name = "GOOG", data_source = "google", start = start, end = end)
 #GOOG is stock name of google.
 
 print(df)
 
 