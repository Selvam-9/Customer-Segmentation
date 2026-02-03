"""
Model Evaluation Script
Evaluates the trained clustering model using multiple metrics
"""
import os
import sys
import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.utils import load_object
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from src.logger import logging as custom_logging

logger = logging.getLogger(__name__)

def evaluate_model():
    """
    Evaluate the trained KMeans clustering model using multiple metrics
    """
    try:
        logger.info("Starting model evaluation...")
        
        # Load model and preprocessor
        model_path = "artifact/model.pkl"
        preprocessor_path = "artifact/preprocessor.pkl"
        
        if not os.path.exists(model_path) or not os.path.exists(preprocessor_path):
            raise FileNotFoundError(f"Model or preprocessor not found. Train the model first using: python run_training.py")
        
        model = load_object(model_path)
        preprocessor = load_object(preprocessor_path)
        logger.info("Model and preprocessor loaded successfully")
        
        # Load and process data
        ingestion = DataIngestion()
        data_path = ingestion.initiate_data_ingestion()[0]
        logger.info(f"Data ingested from {data_path}")
        
        transformation = DataTransformation()
        X_processed = transformation.initiate_data_transformation(data_path)[0]
        logger.info(f"Data transformed. Shape: {X_processed.shape}")
        
        # Get predictions
        labels = model.predict(X_processed)
        logger.info(f"Predictions generated. Number of clusters: {len(set(labels))}")
        
        # Calculate evaluation metrics
        print("\n" + "="*50)
        print("MODEL EVALUATION METRICS")
        print("="*50)
        
        # Silhouette Score (higher is better, range: -1 to 1)
        silhouette = silhouette_score(X_processed, labels)
        print(f"\n✓ Silhouette Score: {silhouette:.4f}")
        print(f"  → Interpretation: Measures how similar an object is to its cluster")
        print(f"     Score > 0.5: Good clustering")
        print(f"     Score > 0.7: Excellent clustering")
        
        # Davies-Bouldin Index (lower is better)
        davies_bouldin = davies_bouldin_score(X_processed, labels)
        print(f"\n✓ Davies-Bouldin Index: {davies_bouldin:.4f}")
        print(f"  → Interpretation: Average similarity between each cluster and its most similar cluster")
        print(f"     Lower values indicate better separation between clusters")
        
        # Calinski-Harabasz Index (higher is better)
        calinski = calinski_harabasz_score(X_processed, labels)
        print(f"\n✓ Calinski-Harabasz Index: {calinski:.4f}")
        print(f"  → Interpretation: Ratio of between-cluster to within-cluster variance")
        print(f"     Higher values indicate better-defined clusters")
        
        # Cluster distribution
        unique, counts = np.unique(labels, return_counts=True)
        print(f"\n✓ Cluster Distribution:")
        for cluster_id, count in zip(unique, counts):
            percentage = (count / len(labels)) * 100
            print(f"  → Cluster {cluster_id}: {count} samples ({percentage:.1f}%)")
        
        print("\n" + "="*50)
        logger.info("Model evaluation completed successfully")
        
        return {
            "silhouette_score": silhouette,
            "davies_bouldin_score": davies_bouldin,
            "calinski_harabasz_score": calinski,
            "cluster_distribution": dict(zip(unique, counts))
        }
        
    except Exception as e:
        logger.error(f"Error during model evaluation: {str(e)}")
        print(f"\n❌ Error occurred: {e}")
        raise e

if __name__ == "__main__":
    import numpy as np
    evaluate_model()
