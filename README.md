# Customer Segmentation - ML Pipeline

An end-to-end machine learning pipeline for customer segmentation using K-Means clustering. This project demonstrates industry-standard practices including data ingestion, transformation, model training, evaluation, and web deployment.

## 📋 Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Pipeline Architecture](#pipeline-architecture)
- [Model Evaluation](#model-evaluation)
- [Web Application](#web-application)
- [Docker Deployment](#docker-deployment)
- [Testing](#testing)
- [Contributing](#contributing)

## 📊 Overview

This project implements a complete ML pipeline to segment mall customers into distinct groups based on their demographics and spending behavior. The model identifies customer segments that can be used for targeted marketing campaigns and personalized customer experiences.

**Dataset:** Mall Customers (200 samples)
**Features:** Gender, Age, Annual Income, Spending Score
**Algorithm:** K-Means Clustering
**Target:** Customer Segmentation

## 🗂️ Project Structure

```
.
├── artifact/                          # Trained models and preprocessor
│   ├── Mall_Customers.csv            # Dataset
│   ├── model.pkl                      # Trained KMeans model
│   └── preprocessor.pkl               # Data preprocessor (scaler + encoder)
│
├── src/                               # Source code
│   ├── components/
│   │   ├── data_ingestion.py         # Load data from CSV
│   │   ├── data_transformation.py    # Preprocessing and feature scaling
│   │   └── model_trainer.py          # KMeans model training
│   ├── pipeline/
│   │   └── predict_pipeline.py       # Prediction interface
│   ├── exception.py                  # Custom exception handling
│   ├── logger.py                     # Logging configuration
│   └── utils.py                      # Utility functions
│
├── tests/                             # Unit tests
│   ├── test_data_ingestion.py
│   ├── test_data_transformation.py
│   ├── test_model_trainer.py
│   └── test_predict_pipeline.py
│
├── notebook/                          # Jupyter notebooks
│   ├── EDA_Mall_Customers.ipynb      # Exploratory Data Analysis
│   └── MODEL TRAINING.ipynb          # Model development notebook
│
├── logs/                              # Application logs
│
├── app.py                             # Streamlit web application
├── run_training.py                    # Training pipeline orchestrator
├── evaluate.py                        # Model evaluation script
├── setup.py                           # Package configuration
├── config.yaml                        # Configuration file
├── requirements.txt                   # Python dependencies
├── .env.example                       # Environment variables template
├── Dockerfile                         # Docker containerization
└── README.md                          # This file
```

## ✨ Features

- **End-to-End Pipeline**: Complete ML workflow from data loading to prediction
- **Data Validation**: Input validation and error handling
- **Model Evaluation**: Multiple clustering metrics (Silhouette, Davies-Bouldin, Calinski-Harabasz)
- **Web UI**: Interactive Streamlit application for predictions
- **Logging & Monitoring**: Comprehensive logging for debugging and monitoring
- **Unit Tests**: Test coverage for all major components
- **Docker Support**: Easy deployment with containerization
- **Configuration Management**: YAML-based configuration for flexibility
- **Professional Code Structure**: Following ML engineering best practices

## 🚀 Installation

### Prerequisites
- Python 3.10+
- pip or conda
- Git

### Step 1: Clone Repository
```bash
git clone https://github.com/Selvam-9/Customer-Segmentation.git
cd Customer-Segmentation
```

### Step 2: Create Virtual Environment
```bash
# Using venv
python -m venv .venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# OR using conda
conda create -n customer-seg python=3.10
conda activate customer-seg
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation
```bash
python -c "import src; print('✓ Installation successful')"
```

## 📖 Usage

### 1. Train the Model
```bash
python run_training.py
```

Output:
```
============================================================
STARTING CUSTOMER SEGMENTATION PIPELINE
============================================================

[Step 1/3] Data Ingestion...
✓ Data loaded from: artifact/Mall_Customers.csv

[Step 2/3] Data Transformation & Preprocessing...
✓ Data transformed. Shape: (200, 5)
✓ Preprocessor saved to: artifact/preprocessor.pkl

[Step 3/3] Model Training...
✓ Model trained successfully
✓ Average Silhouette Score: 0.5542

============================================================
✅ PIPELINE EXECUTION COMPLETED SUCCESSFULLY
============================================================
```

### 2. Evaluate Model Performance
```bash
python evaluate.py
```

Output shows multiple evaluation metrics:
- **Silhouette Score**: Measures cluster cohesion (-1 to 1, higher is better)
- **Davies-Bouldin Index**: Cluster separation metric (lower is better)
- **Calinski-Harabasz Index**: Ratio of cluster variance (higher is better)

### 3. Run Web Application
```bash
streamlit run app.py
```

Then open http://localhost:8501 in your browser

Features:
- Input customer demographics (Gender, Age, Income, Spending Score)
- Get instant cluster prediction
- View customer profile summary

### 4. Run Unit Tests
```bash
pytest tests/ -v
# or with coverage
pytest tests/ --cov=src
```

## 🔄 Pipeline Architecture

### Data Flow
```
Raw Data (CSV)
    ↓
Data Ingestion
    ↓
Data Transformation
  (Scaling + Encoding)
    ↓
Model Training
   (K-Means)
    ↓
Model & Preprocessor Saved
    ↓
Prediction Pipeline
    ↓
Web Application / API
```

### Component Details

#### 1. Data Ingestion (`src/components/data_ingestion.py`)
- Loads data from CSV file
- Validates data integrity
- Returns path to processed data

#### 2. Data Transformation (`src/components/data_transformation.py`)
- Handles categorical encoding (Gender → numerical)
- Scales numerical features (StandardScaler)
- Returns normalized feature matrix

#### 3. Model Training (`src/components/model_trainer.py`)
- Trains K-Means clustering model
- Calculates Silhouette Score
- Saves model and preprocessor for inference

#### 4. Prediction Pipeline (`src/pipeline/predict_pipeline.py`)
- Loads trained model and preprocessor
- Accepts new customer data
- Returns cluster prediction

## 📈 Model Evaluation

The model is evaluated using three complementary metrics:

| Metric | Range | Better | Interpretation |
|--------|-------|--------|-----------------|
| Silhouette Score | -1 to 1 | Higher | Measures how similar an object is to its cluster |
| Davies-Bouldin Index | 0 to ∞ | Lower | Average similarity between each cluster and its most similar cluster |
| Calinski-Harabasz Index | 0 to ∞ | Higher | Ratio of between-cluster to within-cluster variance |

Run `python evaluate.py` to see detailed metrics.

## 🌐 Web Application

### Features
- **Interactive UI**: User-friendly interface built with Streamlit
- **Real-time Predictions**: Get cluster predictions instantly
- **Input Validation**: Validates all user inputs
- **Error Handling**: Graceful error messages
- **Customer Profile**: View summary of submitted customer data

### Running the App
```bash
streamlit run app.py
```

Then navigate to http://localhost:8501

## 🐳 Docker Deployment

### Build Docker Image
```bash
docker build -t customer-segmentation:latest .
```

### Run Container
```bash
docker run -p 8501:8501 customer-segmentation:latest
```

The app will be available at http://localhost:8501

### Docker Compose (Optional)
```yaml
version: '3.8'
services:
  app:
    build: .
    ports:
      - "8501:8501"
    environment:
      - LOG_LEVEL=INFO
```

## 🧪 Testing

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test File
```bash
pytest tests/test_data_ingestion.py -v
```

### Generate Coverage Report
```bash
pytest tests/ --cov=src --cov-report=html
```

### Test Files
- **test_data_ingestion.py**: Tests data loading and validation
- **test_data_transformation.py**: Tests preprocessing pipeline
- **test_model_trainer.py**: Tests model training and saving
- **test_predict_pipeline.py**: Tests prediction interface

## ⚙️ Configuration

Edit `config.yaml` to customize:
- Data file paths
- Model hyperparameters (n_clusters, init method, etc.)
- Feature scaling strategy
- Preprocessing options

Example:
```yaml
model:
  params:
    n_clusters: 5
    init: "k-means++"
    random_state: 42
```

## 🔧 Environment Variables

Copy `.env.example` to `.env` and customize:
```bash
cp .env.example .env
```

Variables:
- `DATA_PATH`: Path to raw data file
- `MODEL_PATH`: Path to save trained model
- `PREPROCESSOR_PATH`: Path to save preprocessor
- `LOG_LEVEL`: Logging level (INFO, DEBUG, WARNING, ERROR)

## 📝 Logging

Application logs are saved to `logs/` directory. Configure logging level in `.env`:
```env
LOG_LEVEL=INFO
```

Log levels:
- **DEBUG**: Detailed information for debugging
- **INFO**: General informational messages
- **WARNING**: Warning messages for potential issues
- **ERROR**: Error messages for failed operations

## 🚨 Error Handling

The application includes custom exception handling:
- **CustomException**: Custom exception with detailed error context
- **Logging**: All errors are logged with traceback
- **Graceful Degradation**: Partial failures don't crash the entire pipeline

## 📊 Clustering Insights

### Cluster Interpretation
After training, the model segments customers into 5 clusters typically representing:
- **Cluster 0**: Low income, Low spending
- **Cluster 1**: High income, Low spending
- **Cluster 2**: Medium income, Medium spending
- **Cluster 3**: Low income, High spending
- **Cluster 4**: High income, High spending

Use these insights for targeted marketing strategies.

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 📧 Contact

For questions or feedback, please reach out via GitHub issues.

## 🎓 Learning Resources

- [K-Means Clustering Explained](https://scikit-learn.org/stable/modules/clustering.html#k-means)
- [Scikit-Learn Documentation](https://scikit-learn.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [ML Pipeline Best Practices](https://ml-ops.systems/)

---

**Last Updated**: February 2026
**Status**: ✅ Production Ready
**Model Version**: 1.0
