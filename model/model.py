import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
from sklearn.metrics import classification_report
import pickle
class Model():
    def __init__(self):
        self.name = "carforst"
        self.model = pickle.load(open("./model/model.sav","rb"))
    def __str__(self):
        return self.name
    def predict(self, data):
        p = self.model.predict_proba([[x for x in data]])
        return str(p[0][1])
    def evaluate(self):
        return NotImplementedError
