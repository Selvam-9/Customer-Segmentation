"""
Unit tests for Prediction Pipeline
"""
import unittest
import numpy as np
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


class TestCustomData(unittest.TestCase):
    """Test cases for CustomData class"""
    
    def test_custom_data_initialization(self):
        """Test if CustomData can be initialized correctly"""
        data = CustomData(
            gender="Male",
            age=30,
            annual_income=50,
            spending_score=60
        )
        self.assertIsNotNone(data)
    
    def test_custom_data_to_dataframe(self):
        """Test if CustomData can be converted to DataFrame"""
        data = CustomData(
            gender="Female",
            age=25,
            annual_income=45,
            spending_score=55
        )
        df = data.get_data_as_data_frame()
        
        self.assertIsNotNone(df)
        self.assertEqual(len(df), 1)
        self.assertIn("Gender", df.columns)
        self.assertIn("Age", df.columns)


class TestPredictPipeline(unittest.TestCase):
    """Test cases for PredictPipeline class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.pipeline = PredictPipeline()
    
    def test_pipeline_initialization(self):
        """Test if PredictPipeline can be initialized"""
        self.assertIsNotNone(self.pipeline)
    
    def test_pipeline_prediction(self):
        """Test if pipeline can make predictions"""
        data = CustomData(
            gender="Male",
            age=30,
            annual_income=50,
            spending_score=60
        )
        df = data.get_data_as_data_frame()
        
        try:
            result = self.pipeline.predict(df)
            self.assertIsNotNone(result)
            self.assertIsInstance(result, (list, np.ndarray))
        except FileNotFoundError:
            # Model not trained yet, skip this test
            self.skipTest("Model not trained yet")
    
    def test_prediction_returns_valid_cluster(self):
        """Test if prediction returns valid cluster ID"""
        data = CustomData(
            gender="Female",
            age=35,
            annual_income=60,
            spending_score=70
        )
        df = data.get_data_as_data_frame()
        
        try:
            result = self.pipeline.predict(df)
            cluster_id = int(result[0])
            self.assertGreaterEqual(cluster_id, 0)
            self.assertLess(cluster_id, 10)  # Assume less than 10 clusters
        except FileNotFoundError:
            self.skipTest("Model not trained yet")


if __name__ == "__main__":
    unittest.main()
