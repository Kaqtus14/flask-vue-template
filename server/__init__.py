import dotenv
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


dotenv.load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", os.urandom(20))
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["CORS_SUPPORTS_CREDENTIALS"] = True
db = SQLAlchemy(app)
CORS(app)

from . import routes
