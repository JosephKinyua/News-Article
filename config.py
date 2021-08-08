import os
class Config:
  NEWS_DETAIL_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

  NEWS_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
  
  NEWS_API = os.environ.get('NEWS_API')