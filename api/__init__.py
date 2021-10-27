from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from .logs import Logger

api = Flask(__name__)
api.config.from_object(Config)
ma = Marshmallow(api)
db = SQLAlchemy(api)
migrate = Migrate(api, db)
log = Logger(__name__)

from api import routes, models
