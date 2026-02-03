import os
import sys
import dill
import pickle
import numpy as np
import pandas as pd

from sklearn.metrics import silhouette_score
from sklearn.model_selection import ParameterGrid
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X, models, param):
    """
    Evaluates clustering models using Silhouette Score.
    No 'y' (target) is required for unsupervised learning.
    """
    try:
        report = {}

        for i in range(len(list(models))):
            model_name = list(models.keys())[i]
            model = list(models.values())[i]
            para_grid = param[model_name]

            best_score = -1
            best_params = None

            # Manual Grid Search for Clustering (GridSearchCV requires 'y')
            for p in ParameterGrid(para_grid):
                model.set_params(**p)
                labels = model.fit_predict(X)
                
                # Silhouette score requires at least 2 clusters
                if len(set(labels)) > 1:
                    score = silhouette_score(X, labels)
                else:
                    score = -1

                if score > best_score:
                    best_score = score
                    best_params = p

            # Re-fit the best version of the model
            model.set_params(**best_params)
            model.fit(X)

            report[model_name] = best_score

        return report

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj) # Using dill for better compatibility
    except Exception as e:
        raise CustomException(e, sys)
