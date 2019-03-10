# -*- coding: utf-8 -*-
from flask import Flask
import feedparser
from flask import render_template

app= Flask(__name__)

journals = ['bbc','elm','abc']

Titles = ['BBC headlines','ABC: Sevilla','El Mundo']

feedbbc = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml')
feedabc = feedparser.parse('http://sevilla.abc.es/rss/feeds/Sevilla_Sevilla.xml')
feedelm = feedparser.parse('http://estaticos.elmundo.es/elmundo/rss/portada.xml')

@app.route("/")
def get_news():
    return render_template("algo.html",bbc=feedbbc['entries'][:5],elm=feedelm['entries'][:5],abc=feedabc['entries'][:5])

@app.route('/journal/<uno>')
def get_news_journal(uno):
    if uno in journals:
        if uno == 'bbc':
            return render_template("algo.html",bbc=feedbbc['entries'][:5],titles=Titles[0]) 
        if uno == 'elm':
            return render_template("algo.html",elm=feedelm['entries'][:5],titles=Titles[2])
        if uno == 'abc':
            return render_template("algo.html",abc=feedabc['entries'][:5],titles=Titles[1])

if __name__ == '__main__':
  app.run(host="0.0.0.0",port=5300,debug=True)

