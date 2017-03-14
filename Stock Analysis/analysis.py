# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:47:33 2017

@author: Haseeb Bhai
"""

from pandas_datareader import data
import datetime as dt
from bokeh.plotting import figure, show, output_file

def inc_dec(close_v, open_v):
    if open_v < close_v:
        value = "Increase"
    elif open_v > close_v:
        value = "Decrease"
    else:
        value = "Same"
    return value

start = dt.datetime(2016, 8, 1)
end = dt.datetime(2016, 9, 16)

df = data.DataReader(name = "GOOG", data_source = "google", start = start, end = end)
 #GOOG is stock name of google.
 
fig = figure(x_axis_type = "datetime", width = 1000, height = 300)
fig.title = "Candlestick Chart"
 
hours_12 = 12*60*60*1000
df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
df["Average"]  = (df.Open + df.Close)/2
df["Height"] = abs(df.Open - df.Close)

fig.rect( df.index[df.Status == "Increase"], df.Average[df.Status == "Increase"], hours_12, df.Height[df.Status == "Increase"], fill_color = "green", line_color = "black")
fig.rect( df.index[df.Status == "Decrease"], df.Average[df.Status == "Decrease"], hours_12, df.Height[df.Status == "Decrease"], fill_color = "red", line_color = "black")
 
output_file("Candle.html")
show(fig)