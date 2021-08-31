from flask import Flask
from distance_blueprint import api_blueprint


app = Flask(__name__)
app.register_blueprint(api_blueprint)
app.run()