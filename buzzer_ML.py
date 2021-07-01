# -*- coding: utf-8 -*-

import joblib
import os
from preprocessing import cleanText
PATH = os.path.abspath(os.path.join(__file__, "../."))


class BuzzerML:
    """Buzzer Machine Learning Module"""

    def __init__(self,dirpath = PATH+"\\"):
        self.model = None
        self.vectorizer = None
        self.dirpath = dirpath
        self.load_model(dirpath+'model\\dtc_word.sav',
                        dirpath+'model\\vectorizer.pickle')

    def load_model(self, model_path, vector_path):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vector_path)
    
    def clean_text(self,text):
        text = cleanText(text)
        return text
    
    def predict (self, text):
        text = self.clean_text(text)
        vector_data= self.vectorizer.transform([text])
        result = self.model.predict(vector_data)
        return result

