# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 10:14:23 2017

@author: Haseeb Bhai
"""
from flask import Flask
# from flask module we are only importing the Flask class
#Flask class have the prototype to handle the web app

app = Flask(__name__)
# Variable to store Flask object

# A decorator: A path on which we can see our web app running "/" shows home
@app.route("/")
def home():
    # Right after the decorator function is returning data to that decorator path
    return "Homepage content goes here!"
    # return the string to the homepage

#another decorator which will shows the about() returning object to the address mentioned in decorator
@app.route("/about/")
def about():
    # Right after the decorator function is returning data to that decorator path
    return "About content goes here!"
    # return the string to the about page
    
# when we run this python script, it assign the __main__ name to this script
# but when we import this script to another script it will assign file name to this Flask object 
if __name__ == "__main__":
    app.run(debug = True)
    #running the flask object to see the results
    