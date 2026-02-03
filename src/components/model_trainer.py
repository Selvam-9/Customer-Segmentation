import os
import sys
from dataclasses import dataclass

from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN 
from sklearn.metrics import silhouette_score

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifact','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, data_array):
        '''
        Trains multiple clustering models and selects the best based on Silhouette Score.
        '''
        try:
            logging.info("Starting Clustering Model Training")
            
            # In K-Means, there is no X and y. The whole array is our feature set.
            X = data_array 

            # Define Clustering Models to test
            # Note: For Mall Customers, K=5 is usually the 'elbow' point.
            models = {
                "KMeans": KMeans(n_init=10, random_state=42),
                "AgglomerativeClustering": AgglomerativeClustering(),
            }

            # Define Hyperparameters to tune
            params = {
                "KMeans": {
                    'n_clusters': [3, 4, 5, 6, 7],
                    'init': ['k-means++', 'random']
                },
                "AgglomerativeClustering": {
                    'n_clusters': [3, 4, 5, 6, 7],
                    'linkage': ['ward', 'complete', 'average']
                }
            }

            # In industry, we evaluate clustering using Silhouette Score
            # (Range -1 to 1: closer to 1 means clusters are well apart)
            model_report = {}

            for model_name, model in models.items():
                param_grid = params[model_name]
                
                # Simple grid search loop for clustering
                best_s_score = -1
                best_cluster_model = None

                # Testing different cluster counts
                for n in param_grid['n_clusters']:
                    model.set_params(n_clusters=n)
                    labels = model.fit_predict(X)
                    
                    # Calculate Silhouette Score
                    score = silhouette_score(X, labels)
                    
                    if score > best_s_score:
                        best_s_score = score
                        best_cluster_model = model
                
                model_report[model_name] = {
                    "score": best_s_score,
                    "model_obj": best_cluster_model
                }

            # Select the absolute best model across all types
            best_model_name = max(model_report, key=lambda x: model_report[x]['score'])
            best_model_info = model_report[best_model_name]
            
            best_model_score = best_model_info['score']
            best_model = best_model_info['model_obj']

            if best_model_score < 0.3: # Threshold for 'decent' clustering
                raise CustomException("No high-quality clusters found (Silhouette Score too low)")

            logging.info(f"Best Model: {best_model_name} with Silhouette Score: {best_model_score}")

            # Save the best clustering model
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            return best_model_score

        except Exception as e:
            raise CustomException(e, sys)