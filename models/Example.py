import pickle
import pandas as pd
class Example():
    def __init__(self):
        self.name = "Example"
        #self.model = pickle.load(open("./models/pickles/"+self.name+".model.sav","rb"))
        #self.scaler = pickle.load(open("./models/pickles/"+self.name+".scaler.sav","rb"))
    def __str__(self):
        return self.name
    def predict(self, data):
        #data = self.scaler.transform(data)
        #probabilities = self.model.predict_proba(data)
        return  [[0,1] for x in range(len(data))]
