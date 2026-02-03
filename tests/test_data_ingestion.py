"""
Unit tests for Data Ingestion component
"""
import unittest
import os
import pandas as pd
from src.components.data_ingestion import DataIngestion


class TestDataIngestion(unittest.TestCase):
    """Test cases for DataIngestion class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.ingestion = DataIngestion()
    
    def test_data_ingestion_file_exists(self):
        """Test if data file exists"""
        self.assertTrue(os.path.exists("artifact/Mall_Customers.csv"), 
                       "Data file not found")
    
    def test_data_ingestion_returns_path(self):
        """Test if data ingestion returns valid data path"""
        data_path, _ = self.ingestion.initiate_data_ingestion()
        self.assertIsNotNone(data_path)
        self.assertTrue(os.path.exists(data_path))
    
    def test_data_ingestion_returns_dataframe(self):
        """Test if ingested data is a valid DataFrame"""
        data_path, _ = self.ingestion.initiate_data_ingestion()
        df = pd.read_csv(data_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
    
    def test_data_has_required_columns(self):
        """Test if data has all required columns"""
        data_path, _ = self.ingestion.initiate_data_ingestion()
        df = pd.read_csv(data_path)
        required_columns = ["CustomerID", "Gender", "Age", "Annual Income (k$)", "Spending Score (1-100)"]
        for col in required_columns:
            self.assertIn(col, df.columns, f"Column {col} not found in data")
    
    def test_data_no_missing_values_in_features(self):
        """Test if feature columns have no missing values"""
        data_path, _ = self.ingestion.initiate_data_ingestion()
        df = pd.read_csv(data_path)
        feature_columns = ["Gender", "Age", "Annual Income (k$)", "Spending Score (1-100)"]
        for col in feature_columns:
            self.assertEqual(df[col].isnull().sum(), 0, f"Missing values found in {col}")


if __name__ == "__main__":
    unittest.main()
