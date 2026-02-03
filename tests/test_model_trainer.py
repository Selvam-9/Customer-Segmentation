"""
Unit tests for Model Trainer component
"""
import unittest
import os
import numpy as np
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class TestModelTrainer(unittest.TestCase):
    """Test cases for ModelTrainer class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.ingestion = DataIngestion()
        self.transformation = DataTransformation()
        self.trainer = ModelTrainer()
        
        # Prepare data
        data_path = self.ingestion.initiate_data_ingestion()[0]
        self.X_processed, _ = self.transformation.initiate_data_transformation(data_path)
    
    def test_model_training_returns_score(self):
        """Test if model training returns a valid score"""
        score = self.trainer.initiate_model_trainer(self.X_processed)
        self.assertIsNotNone(score)
        self.assertIsInstance(score, (int, float))
    
    def test_model_file_is_saved(self):
        """Test if trained model is saved"""
        self.trainer.initiate_model_trainer(self.X_processed)
        self.assertTrue(os.path.exists("artifact/model.pkl"), "Model file not saved")
    
    def test_model_predictions(self):
        """Test if model can make predictions"""
        self.trainer.initiate_model_trainer(self.X_processed)
        from src.utils import load_object
        
        model = load_object("artifact/model.pkl")
        predictions = model.predict(self.X_processed)
        
        self.assertEqual(len(predictions), len(self.X_processed))
        self.assertTrue(all(isinstance(p, (int, np.integer)) for p in predictions))
    
    def test_cluster_count(self):
        """Test if model creates expected number of clusters"""
        self.trainer.initiate_model_trainer(self.X_processed)
        from src.utils import load_object
        
        model = load_object("artifact/model.pkl")
        predictions = model.predict(self.X_processed)
        n_clusters = len(set(predictions))
        
        # Default n_clusters should be around 5
        self.assertGreater(n_clusters, 1, "Model should create multiple clusters")
        self.assertLessEqual(n_clusters, 10, "Number of clusters seems too high")


if __name__ == "__main__":
    unittest.main()
