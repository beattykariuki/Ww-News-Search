class Config:

    HEADLINES_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'
    SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    SEARCH_API = 'https://newsapi.org/v2/everything?q={}&pageSize=1&apiKey={}'
    SOURCE_ARTICLES = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"

class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG = True
