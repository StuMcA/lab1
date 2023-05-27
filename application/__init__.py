from flask import Flask

app = Flask(__name__)

from application import config
#  import application config

from application import routes

