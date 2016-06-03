from flask import Flask
from settings import DEBUG, SECRET_KEY

app = Flask(__name__)
app.config['DEBUG'] = DEBUG
app.config['SECRET_KEY'] = SECRET_KEY

import copaticket.views
