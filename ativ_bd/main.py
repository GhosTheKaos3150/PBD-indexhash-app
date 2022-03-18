from distutils.log import debug
from flask import Flask
from flask_cors import CORS
from routes.hash_route import hash_route
from routes.index import index_route

if __name__ == "__main__":

    app = Flask(__name__)
    CORS(app)
    
    app.register_blueprint(hash_route)
    app.register_blueprint(index_route)

    app.run(host="localhost", port="3150", debug=True)
