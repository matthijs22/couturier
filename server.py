from flask import Flask, request
from flask_restful import Resource, Api

from model.model import Model

import json


app = Flask(__name__)
api = Api(app)

tm = Model()

class Model(Resource):
    def get(self):
        return {"Model":tm.name,"Status": "Running"}, 200
class Predict(Resource):
    def get(self):
        return "Post requests only"
    def post(self):
        data = request.json
        try:
            return tm.predict(data), 200
        except ValueError:
            return "ValueError: Inputshape incorrect", 500
        else:
            return "An error occurred", 500

api.add_resource(Model, '/model')
api.add_resource(Predict, '/predict')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)