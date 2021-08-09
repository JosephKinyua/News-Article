import urllib.request, json
from app.models import Article, Source

api_key = None
base_url = None
detail_url = None

def configure_request(app):
    global base_url, detail_url, api_key