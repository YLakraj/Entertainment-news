
from flask import Flask, request,render_template

from flask_pymongo import PyMongo
from pymongo import MongoClient
from newsdataapi import NewsDataApiClient
from newsapi import NewsApiClient

import  requests

app = Flask(__name__)



@app.route('/',methods=['GET','POST'])
def helloworld():

    username = request.form.get('username')
    if request.method == 'POST' and  request.form.get('username'):
      return render_template("Home.html", username=username)


    return render_template("index.html")


@app.route('/astrology',methods=['GET','POST'])
def astrology():
    url = "https://newsapi.org/v2/everything?q=Astronomy&from=newest&sortBy=popularity&apiKey=a4ae3210d8d64a0fa0791bf26346c360"
    r = requests.get(url).json()
    cases = {
        'articles': r['articles']

    }

    return render_template("astrology.html",case=cases)

@app.route('/entertainment',methods=['GET','POST'])#
def entertainment():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=a4ae3210d8d64a0fa0791bf26346c360"
    r = requests.get(url).json()
    cases = {
        'articles': r['articles']

    }

    return render_template("ent.html",case=cases)

@app.route('/techology',methods=['GET','POST'])
def techology():

    url = "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=a4ae3210d8d64a0fa0791bf26346c360"
    r = requests.get(url).json()
    cases = {
        'articles': r['articles']

    }
    return render_template("tech.html", case = cases)

@app.route('/weather',methods=['GET','POST'])#,methods=['GET','POST']#
def bbc():
    url = "https://newsapi.org/v2/everything?q=climate&weather&from=newest&sortBy=newest&apiKey=a4ae3210d8d64a0fa0791bf26346c360"
    r = requests.get(url).json()
    cases = {
        'articles': r['articles']

    }

    return render_template("weather.html",case=cases)



app.run()