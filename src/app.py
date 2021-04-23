from flask import Flask
from flask_restful import Api
from api.routes import initialize_routes
from database.db import initialize_db

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

initialize_db(app)
initialize_routes(api)

app.run()
