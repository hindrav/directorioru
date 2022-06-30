from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI
from flask_bs4 import Bootstrap

app = Flask(__name__)

Bootstrap = Bootstrap(app)

# Settings
app.secret_key = 'mysecret'
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# No cache
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

SQLAlchemy(app)

app.register_blueprint(contacts)