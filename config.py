import os

class Config:
    '''
    General configuration parent class
    '''
    # NEWS_API_KEY = '5012e1c88574424db29c6106b935bc1e'
    # NEWS_API_BASE_URL = 'https://newsapi.org/v2/everything?sources?api_key=5012e1c88574424db29c6106b935bc1e'
    NEWS_HIGHLIGHT_API_BASE_URL ='https://newsapi.org/v2/sources?apiKey={}'
    TOP_HEADLINES_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    EVERYHTHING_URL ='https://newsapi.org/v2/everything?q=bitcoin&apiKey={}'
    NEWS_HIGHLIGHT_API_URL= os.environ.get('NEWS_HIGHLIGHT_API_KEY')
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
config_options = {
  'development' : DevConfig,
  'production' : ProdConfig
}