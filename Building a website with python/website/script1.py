# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 10:14:23 2017

@author: Haseeb Bhai
"""
from flask import Flask, render_template
# from flask module we are only importing the Flask class and render_template class
#Flask class have the prototype to handle the web app
# render_template is used to return the html,css, js templates to web app

app = Flask(__name__)
# Variable to store Flask object

# A decorator: A path on which we can see our web app running "/" means home
@app.route("/")
def home():
    return render_template("home.html")
    # returing the home.html file from templaes folder

#another decorator which will shows the about() returning object to the address mentioned in decorator
@app.route("/about/")
def about():
    return render_template("about.html")
    # returning the about.html from templates folder
    
# when we run this python script, it assign the __main__ name to this script
# but when we import this script to another script it will assign file name to this Flask object 
if __name__ == "__main__":
    app.run(debug = True)
    #running the flask object to see the results

    