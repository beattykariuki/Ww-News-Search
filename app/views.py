# from flask import render_template
from app import app
from .request import get_news,search_news,search_sources
from flask import render_template,request,redirect,url_for
from .models import news
from .forms import ReviewForm
# Review = review.Review

@app.route('/')
def index():
   
    business_results_list = search_sources('business')
    entertainment_results_list = search_sources('entertainment')
    health_news_list = search_sources('health')
    technology_results_list = search_sources('technology')
    title = 'News Search'
    search_news = request.args.get('')

    print(type(business_results_list) == list)
    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title = title, business=business_results_list, entertainment = entertainment_results_list, health= health_news_list, technology = technology_results_list)

@app.route('/news/<title>')
def news_title(title):

    # news = search_article(title)

    title = f'{news.title}'
    
    return render_template('news.html',title = title,news = news)

@app.route('/search/<news_name>')
def search(news_name):

    news_name_list = news_name.spilt("")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)

@app.route('/news/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    news = get_news(id)

    if form.validate_on_submit():
        title = form.title.data
        
        
        return redirect(url_for('news',id = news.title ))

    title = f'{news.title} review'
    return render_template('new_review.html',title = title, review_form=form, news=news)  

@app.route("/articles/<id>")
def articles(id):

    articles = get_news(id)

    return render_template("news.html", articles = articles)