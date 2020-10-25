from os import listdir
from os.path import isfile, join
from pydoc import locate

class ModelManager:
    _models = []
    
    def __init__(self):
        """Construct the model manager
        
        This function retrieves all python files in the models folder and 
        adds instances of each modelclass to the models list
        """

        modelnames = [f[:-3] for f in listdir("./models/") if isfile(join("./models/", f)) and f[-2:]=="py"]
        for modelname in modelnames:
            self._load_model(modelname)
    def _load_model(self, modelname):
        """Locates and instantiates a model

        This function loads the model file and instantiates the class
        Instantiated class is added to the models list
        """

        model_class = locate('models.'+modelname+'.'+modelname)
        self._models.append(model_class())

    def get_models(self):
         """Returns the models list"""
         
         return self._models
         
    def get_model(self,name):
        """Returns a model by name"""
        try:
            return list(filter(lambda m: m.name == name,self._models))[0]
        except(IndexError):
            raise IndexError("Model not found")