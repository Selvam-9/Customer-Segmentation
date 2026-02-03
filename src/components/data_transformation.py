import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifact','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        Creates a robust pipeline for unsupervised clustering.
        Feature scaling is critical for K-Means distance metrics.
        '''

        try:
            #update Mall Customer dataset
            numberical_columns = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
            categorical_columns = ["Gender"]

            #Numberical Pipeline: StandardScaler is Critical for K-Means Distance
            num_pipline = Pipeline(
                steps=[('imputer',SimpleImputer(strategy='median')),
                       ('scaler',StandardScaler())]
            )

            #Categorical Pipeline: Convert Gender to numberical format 
            cat_pipline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder',OneHotEncoder(handle_unknown='ignore')),
                    ('scaler',StandardScaler(with_mean=False))
                ]
            )

            logging.info(f'Categorical columns:{categorical_columns}')
            logging.info(f'Numberical columns:{numberical_columns}')

            #Combine the pipline
            preprocessor = ColumnTransformer(
                [('num_pipeline',num_pipline,numberical_columns),
                 ('cat_pipeline',cat_pipline,categorical_columns)]
            )
            return preprocessor
        except Exception as e:
            raise CustomException (e,sys)
    def initiate_data_transformation(self,data_path):
        'Processing the raw data for clustring'
        try:
            #load the dataset
            df = pd.read_csv(data_path)
            logging.info(f'Read data from the {data_path} completed')

            #Obtain preporcessor
            preprocessing_obj = self.get_data_transformer_object()

            #Drop unique idendifier (CustomerID) before clustering
            #They provide no geometric information and can confuse the model.
            data_to_transform = df.drop(columns=['CustomerID'],errors='ignore')

            logging.info('Applying the preprocessing object on the dataset')

            #Transform the data into a pure numerical matrix
            preprocessed_arr = preprocessing_obj.fit_transform(data_to_transform)

            #Save the preprocesssor for future inference (predicting new customer clusters)
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return(
                preprocessed_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        

