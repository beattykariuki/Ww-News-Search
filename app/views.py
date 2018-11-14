from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():

    popular_news = get_news('popular')
    print(popular_news)
    title = 'Home - Welcome To News Search'
    return render_template('index.html', title = title,popular = popular_news)

@app.route('/news/<int:news_id>')
def news(news_id):

    return render_template('news.html',id = news_id)
