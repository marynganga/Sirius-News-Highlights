from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

# Initialize flask extensions
bootstrap = Bootstrap()

def create_app(config_name):
	# initialize application
	app = Flask(__name__)

	# set up configurations
	app.config.from_object(config_options[config_name])
	app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

	# initialize flask extensions
	bootstrap.init_app(app)

	# registering the blueprint
	from .main import main as main_blueprint

	app.register_blueprint(main_blueprint)

	# setting config 
	from .request import configure_request
	configure_request(app)

	return app 