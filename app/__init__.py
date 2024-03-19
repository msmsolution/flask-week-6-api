from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_restful import Api

from .api.student import StudentResource

app = Flask(__name__)
api = Api(app, prefix="/api")

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

api.add_resource(StudentResource, "/student")

from app import routes, models



def create_app(config_class=Config):
    app = Flask(__name__)
    from app.api_blueprint import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')