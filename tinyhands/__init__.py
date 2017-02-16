import os
from flask import Flask
from flask_restful import Api

# Initialize application
app = Flask(__name__)

# Initialize extensions
api = Api(app)

# Load configuration
app.config.from_object(__name__)
app.config.update(dict(
	SECRET_KEY='for the love of osm',
	USERNAME='admin',
	PASSWORD='default'
))
app.config.from_envvar('TINYHANDS_SETTINGS', silent=True)

# Add API routes
from tinyhands.resources.bug import Bug
api.add_resource(BugAPI, '/bug', '/bug/<string:id>')

if __name__ == '__main__':
	app.run()