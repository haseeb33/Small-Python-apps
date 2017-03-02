# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 09:02:03 2017

@author: Haseeb Bhai
"""
import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc"
#r"string": r stands for row so if we have \n in it. it's part of string
# but without r \n will be read as newline

redirect = "127.0.0.1"
#websites will redirect to this address

website_list = ["www.facebook.com", "facebook.com",
                "www.twitter.com", "twitter.com"] 

year = dt.now().year
month = dt.now().month
day = dt.now().day
            
start_hr = 8
end_hr = 16
while True:
    if dt(year, month, day, start_hr) < dt.now() < dt(year, month, day, end_hr):
        print("Working hours")
        file = open(hosts_temp, "r+")
        content = file.read()
        for website in website_list:
            if not website in content:
                file.write(redirect + "       " + website + "\n")
    else: 
        file = open(hosts_temp, "r+")
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()
        print("Fun hours")
    time.sleep(5)
