"""
Unit tests for Data Transformation component
"""
import unittest
import numpy as np
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation


class TestDataTransformation(unittest.TestCase):
    """Test cases for DataTransformation class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.ingestion = DataIngestion()
        self.transformation = DataTransformation()
        self.data_path = self.ingestion.initiate_data_ingestion()[0]
    
    def test_data_transformation_returns_array(self):
        """Test if transformation returns numpy array"""
        X_processed, _ = self.transformation.initiate_data_transformation(self.data_path)
        self.assertIsInstance(X_processed, np.ndarray)
    
    def test_transformed_data_shape(self):
        """Test if transformed data has correct shape"""
        X_processed, _ = self.transformation.initiate_data_transformation(self.data_path)
        # After encoding Gender (M/F) -> 2 columns and 3 numerical features = 5 total
        self.assertGreater(X_processed.shape[1], 3, "Transformed data should have more than 3 features")
        self.assertGreater(X_processed.shape[0], 0, "Transformed data should have samples")
    
    def test_transformed_data_no_nan(self):
        """Test if transformed data has no NaN values"""
        X_processed, _ = self.transformation.initiate_data_transformation(self.data_path)
        self.assertEqual(np.isnan(X_processed).sum(), 0, "NaN values found in transformed data")
    
    def test_transformed_data_is_numeric(self):
        """Test if transformed data contains numeric values"""
        X_processed, _ = self.transformation.initiate_data_transformation(self.data_path)
        self.assertTrue(np.issubdtype(X_processed.dtype, np.number), 
                       "Transformed data should be numeric")
    
    def test_preprocessor_is_saved(self):
        """Test if preprocessor object is saved"""
        import os
        _, preprocessor_path = self.transformation.initiate_data_transformation(self.data_path)
        self.assertTrue(os.path.exists(preprocessor_path), "Preprocessor file not saved")


if __name__ == "__main__":
    unittest.main()
