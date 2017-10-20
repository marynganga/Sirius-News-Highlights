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

def get_sources(category):
	'''
	Function that gets the json response to our url request
	'''
	get_sources_url = sources_base_url.format(category)

	with urllib.request.urlopen(get_sources_url,data=None) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)
		sources_results = None

		if get_sources_response['sources']:
			sources_results_list = get_sources_response['sources']
			sources_results = process_results(movie_results_list)

	return sources_results

def process_results()