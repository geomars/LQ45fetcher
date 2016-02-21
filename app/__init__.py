# project/app/__init__.py 

#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import Flask

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
app = Flask(__name__, instance_relative_config=True)

# Load the base configuration
app.config.from_object('config.base')


from app import views