class Config:

    HEADLINES_BASE_URL = 'https://newsapi.org/v2/top-headlines?category={}country=us&apiKey={}'
    SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    pass

class ProdConfig(Config):

    pass

class DevConfig(Config):

    pass

    DEBUG = True