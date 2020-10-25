from flask import Flask, request
from flask_restful import Resource, Api
import json
from model_manager import ModelManager

app = Flask(__name__)
api = Api(app)

manager = ModelManager()

class StatusInfo(Resource):
    def get(self):
        return {"Models":[model.name for model in manager.get_models()],"Status": "Running"}, 200

class Model(Resource):
    def get(self):
# class Predict(Resource):
#     def get(self):
#         return "Post requests only"
#     def post(self):
#         data = request.json
#         try:
#             return tm.predict(data), 200
#         except ValueError:
#             return "ValueError: Inputshape incorrect", 500
#         else:
#             return "An error occurred", 500

api.add_resource(StatusInfo, '/')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)