import sys
import os
import logging

import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path = os.path.join('artifact','model.pkl')
            preprocessor_path = os.path.join('artifact','preprocessor.pkl')

            logging.info('Loading model and preprocessor')
            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            #Transform input features usign the saved scaler/encoder
            data_scaled = preprocessor.transform(features)

            #Model.predict will return the Cluster group
            cluster_assignment = model.predict(data_scaled)

            return cluster_assignment
            
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(self, gender:str,age:int,annual_income:int,spending_score:int):
        'class to map web/ui input to the model features'

        self.gender = gender
        self.age = age
        self.annual_income = annual_income
        self.spending_score = spending_score
    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict={
            'Gender':[self.gender],
            'Age':[self.age],
            'Annual Income (k$)':[self.annual_income],
            'Spending Score (1-100)':[self.spending_score],
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)