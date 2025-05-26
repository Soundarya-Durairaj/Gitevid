from flask import Flask
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = '3d9f1c8ae23c4b72a5e6bb9d64f0c8d3'

csrf = CSRFProtect(app)

from app import routes
