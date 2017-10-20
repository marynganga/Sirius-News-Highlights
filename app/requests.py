import urrlib.request,json
from .models import Source,Article

# Getting Api Key
api_Key = None
#Getting the base urls
sources_base_url = None
articles_base_url = None

def configure_request(app):
	'''
	Function to acquire the api key and base urls
	'''
	global api_Key,sources_base_url,articles_base_url
	api_Key = app.config['NEW_API_KEY']
	sources_base_url = app.config['NEWS_SOURCES_BASE_URL']
	articles_base_url = app.config['NEWS_ARTICLES_BASE_URL']
	