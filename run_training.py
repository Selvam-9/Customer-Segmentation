"""
Complete ML Pipeline for Customer Segmentation
Orchestrates data ingestion, transformation, and model training
"""
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logging

logger = logging.getLogger(__name__)


def run_pipeline():
    """
    Execute the complete ML pipeline:
    1. Data Ingestion - Load data from CSV
    2. Data Transformation - Clean, preprocess, and scale data
    3. Model Training - Train KMeans clustering model
    """
    try:
        print("\n" + "="*60)
        print("STARTING CUSTOMER SEGMENTATION PIPELINE")
        print("="*60)
        
        # Step 1: Data Ingestion
        print("\n[Step 1/3] Data Ingestion...")
        logger.info("Starting Data Ingestion")
        ingestion = DataIngestion()
        data_path, _ = ingestion.initiate_data_ingestion()
        logger.info(f"✓ Data ingested successfully from: {data_path}")
        print(f"✓ Data loaded from: {data_path}")
        
        # Step 2: Data Transformation
        print("\n[Step 2/3] Data Transformation & Preprocessing...")
        logger.info("Starting Data Transformation")
        transformation = DataTransformation()
        processed_arr, preprocessor_path = transformation.initiate_data_transformation(data_path)
        logger.info(f"✓ Data transformed. Shape: {processed_arr.shape}")
        logger.info(f"✓ Preprocessor saved to: {preprocessor_path}")
        print(f"✓ Data transformed. Shape: {processed_arr.shape}")
        print(f"✓ Preprocessor saved to: {preprocessor_path}")
        
        # Step 3: Model Training
        print("\n[Step 3/3] Model Training...")
        logger.info("Starting Model Training")
        trainer = ModelTrainer()
        silhouette_avg = trainer.initiate_model_trainer(processed_arr)
        logger.info(f"✓ Model trained successfully")
        logger.info(f"✓ Average Silhouette Score: {silhouette_avg:.4f}")
        print(f"✓ Model trained successfully")
        print(f"✓ Average Silhouette Score: {silhouette_avg:.4f}")
        
        print("\n" + "="*60)
        print("✅ PIPELINE EXECUTION COMPLETED SUCCESSFULLY")
        print("="*60)
        print(f"\nModel saved to: artifact/model.pkl")
        print(f"Next steps:")
        print("  1. Run evaluation: python evaluate.py")
        print("  2. Start web app: streamlit run app.py")
        print("  3. Run tests: pytest tests/")
        print("="*60 + "\n")
        
        return True
        
    except Exception as e:
        logger.error(f"Pipeline execution failed: {str(e)}", exc_info=True)
        print(f"\n❌ PIPELINE EXECUTION FAILED")
        print(f"Error: {str(e)}")
        print("="*60 + "\n")
        return False


if __name__ == "__main__":
    success = run_pipeline()
    sys.exit(0 if success else 1)
