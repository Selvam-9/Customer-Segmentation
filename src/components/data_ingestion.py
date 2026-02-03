# Read csv file and load data into pandas DataFrame
# train and test split 
# save in a folder

import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('artifact','Mall_Customers.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion methos or component')
        try:
           df = pd.read_csv(r'C:\Users\selvam.anandhan\OneDrive - IDP Education Ltd\Documents\DS\myproject\artifact\Mall_Customers.csv')
           logging.info('Read the dataset as dataframe')

           os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
           df.to_csv(self.ingestion_config.raw_data_path, index=False)
           logging.info('Raw data is saved')
           
           return self.ingestion_config.raw_data_path, self.ingestion_config.raw_data_path

        except Exception as e:
            logging.info('Exception occured in the data ingestion componet')
            raise CustomException (e,sys)
        
