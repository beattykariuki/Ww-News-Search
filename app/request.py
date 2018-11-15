from app import app 
import urllib.request,json
from .models import news
from .models.sources import Sources
News = news.News

api_key = app.config['NEWS_API_KEY']

base_url = app.config['HEADLINES_BASE_URL']
search_api = app.config["SEARCH_API"]
sources_api = app.config["SOURCES_BASE_URL"]
source_articles_api = app.config["SOURCE_ARTICLES"]

def get_news(id):
        
        get_news_url = source_articles_api.format(id,api_key)

        with urllib.request.urlopen(get_news_url) as url:
            get_news_data = url.read()
            get_news_response = json.loads(get_news_data)
            

            news_results = None

            if get_news_response['articles']:
                news_results_list = get_news_response['articles']
                news_results = process_results(news_results_list)

        return news_results

def process_results(news_list):
        
        news_results = []
        for news_item in news_list:
            author = news_item.get('author')
            title = news_item.get('title')
            description = news_item.get('description')
            url = news_item.get('url')
            urlToImage = news_item.get('urlToImage')
            publishedAt = news_item.get('publishedAt')
            content = ('content')

            if author and urlToImage and content:
                news_object = News(author,title,description,url,urlToImage,publishedAt,content)
                news_results.append(news_object)
        return news_results
        
def get_news_details():
    get_news_details_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
           author = news_details_response.get('author')
           title = news_details_response.get('title')
           description = news_details_response.get('description')
           url = news_details_response.get('url')
           urlToImage = news_details_response.get('urlToImage')
           publishedAt = news_details_response.get('publishedAt')
           content = news_details_response.get('content')

           news_object = News(author,title,description,url,urlToImage,publishedAt,content)

        return news_object

def search_news(news_name):
    search_news_url = base_url.format(id,api_key)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_results(search_news_list)

        return search_news_results 

def search_sources(category):
        sources_url = sources_api.format(category,api_key)

        with urllib.request.urlopen(sources_url) as url:
                sources_data = url.read()
                sources_response = json.loads(sources_data)

                sources_results = None

                if sources_response["sources"]:
                        sources_list = sources_response["sources"]
                        sources_results = process_sources(sources_list)
        return sources_results
def process_sources(sources_list):

        results = []
        for source in sources_list:
                id = source.get("id")
                name = source.get("name")
                category = source.get("category")
                url = source.get("url")
                description = source.get("description")
                new_source = Sources(id,name,url,category,description)
                results.append(new_source)

        return results

