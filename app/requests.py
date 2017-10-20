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
			sourcesq_results = process_results(movie_results_list)

	return sources_results

def process_results(sources_results):
	'''
    Function  that processes the sources result and transform them to a list of Objects

    Args:
        sources_results: A list of dictionaries that contain sources details

    Returns :
        sources_list: A list of sources objects
    '''
    sources_list = []
    for source_item in sources_results:
    	id = source_item.get('id')
    	name = source_item.get('name')
    	description = source_item.get('description')
    	url = source_item.get('url')
    	category = source_item.get('category')

    	source_object = Source(id,name,description,url,category)
    	sources_list.append(source_object)

    return sources_list



