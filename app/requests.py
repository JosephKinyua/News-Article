import urllib.request, json
from app.models import Article, Source

api_key = None
base_url = None
detail_url = None

def configure_request(app):
    global base_url, detail_url, api_key
    api_key = app.config['NEWS_API']
    base_url = app.config['NEWS_BASE_URL']
    detail_url = app.config['NEWS_DETAIL_URL']
    
def get_sources(sources):
    get_source_url = base_url.format(sources, api_key)
    print(get_source_url)
    try:
        with urllib.request.urlopen(get_source_url) as url:
            get_catergory_data = url.read()
            get_catergory_response = json.loads(get_catergory_data)
            
            news_data = None
            
            if get_catergory_response['sources']:
                news_list = get_catergory_response['sources']
                news_data = extractData(news_list)
        return news_data
    except urllib.error.URLError:
        print('Connection Reset by peer')
    except TypeError:
        print('Too many Request to API. Wait for 24 hrs or Upgrade to Premium')
def extractData(newsList):
     news_list = []
        


    
    
  