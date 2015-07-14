from flask import Flask
from flask.ext import restful
from flask.ext.restful import Api
app = Flask(__name__)
app.config.from_object('config')
#flask­sqlalchemy
db = SQLAlchemy(app)
#flask­restful
api = restful.Api(app)

@app.after_request
def after_request(response):
    response.headers.add('Access­Control­Allow­Origin', '*')
    return response
import views