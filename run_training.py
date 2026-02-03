from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logging

if __name__ == "__main__":
    try:
        # 1. Data Ingestion
        # Even in clustering, we can ingest data from a source (CSV/Database)
        ingestion = DataIngestion()
        data_path, _ = ingestion.initiate_data_ingestion()

        # 2. Data Transformation
        # We process the data into a scaled numerical matrix
        transformation = DataTransformation()
        # We only need one array for clustering, not a train/test split
        processed_arr, _ = transformation.initiate_data_transformation(data_path)

        # 3. Model Training
        # The trainer now finds the best clusters and returns the Silhouette Score
        trainer = ModelTrainer()
        silhouette_avg = trainer.initiate_model_trainer(processed_arr)
        
        print(f"Training complete.")
        print(f"Average Silhouette Score: {silhouette_avg:.4f}")
        logging.info(f"Model Training Pipeline completed with Silhouette Score: {silhouette_avg}")

    except Exception as e:
        print(f"Error occurred: {e}")
