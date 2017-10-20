class Source:
	'''
	Source Class to define Source Objects
	'''
	def __init__(self,id,name,description,url,category):
		'''
		Function to initialize Source Objects
		Args: 
			1. id
			2. name
			3. description
			4. url 
			5. category
		'''
		self.id = id
		self.name = name
		self.description = description
		self.url = url
		self.category = category

