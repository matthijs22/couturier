from flask import Flask, request
from flask_restful import Resource, Api
from model_manager import ModelManager
from config_manager import ConfigManager

app = Flask(__name__)
api = Api(app)

manager = ModelManager()
config = ConfigManager()

class ModelList(Resource):
    def get(self):
        return {"Models":[model.name for model in manager.get_models()],"Status": "Running"}, 200

class Model(Resource):
    def get(self, name):
        try:
            return manager.get_model(name).name, 200
        except(IndexError):
            return "Model not found", 404

class Predict(Resource):
    def get(self, name):
        return "Post requests only" 
    def post(self, name):
        data = request.json
        try:
            model = manager.get_model(name)
            return model.predict(data),200
        except IndexError:
            return "Model not found", 404
        except ValueError:
            return "Inputshape incorrect", 500
        else:
            return "An unkown error occurred", 500

api.add_resource(ModelList, '/','/model')
api.add_resource(Model, '/model/<string:name>')
api.add_resource(Predict, '/model/<string:name>/predict')

if __name__ == '__main__':
    app.run(debug=config.get("debug"),host=config.get("host"),port=config.get("port"))