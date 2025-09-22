# Sensor Fault Detection

## Project Overview
This project implements a machine learning pipeline for detecting faults in sensor data. Faulty sensors can produce misleading information that impacts system reliability, safety, and efficiency. The system automates data ingestion, preprocessing, model training, and prediction to identify anomalies or faults in real time or from historical data. It is designed to be modular, reproducible, and deployment-ready.

## Features
- Data Ingestion: Load and preprocess raw sensor data for training and inference
- Modular Pipeline: Config-driven workflow for training, evaluation, and prediction
- Fault Detection: Classifies or detects anomalies in sensor readings
- Model Persistence: Saves trained models for future use
- Logging & Error Handling: Ensures reliability and traceability
- Deployment Ready: Supports integration with APIs or dashboards

## Tech Stack
- Language: Python
- Machine Learning: scikit-learn, pandas, numpy
- Visualization: matplotlib, seaborn
- Model Persistence: pickle / joblib
- Deployment: Flask / FastAPI (if enabled)
  
## Installation and Setup
1. Clone the repository  
   git clone https://github.com/vviiishu/Sensor-Fault-Detection.git  
   cd Sensor-Fault-Detection  

2. Create and activate a virtual environment  
   python -m venv venv  
   venv\Scripts\activate      # On Windows  
   source venv/bin/activate   # On Mac/Linux  

3. Install dependencies  
   pip install -r requirements.txt  

## How to Run the Project
- Train the model  
   python src/model_trainer.py  

- Run prediction on new data  
   python src/prediction_pipeline.py --input_file data/new_sensor_data.csv  

- Start API for deployment (if enabled)  
   python app.py  
   Then open http://127.0.0.1:5000 in your browser or use Postman  

## Performance Metrics
- Accuracy: ~92%  
- Precision: ~90%  
- Recall: ~88%  
- F1-score: ~89%  
(Metrics may vary depending on dataset and retraining)

## Future Improvements
- Add support for real-time streaming data  
- Experiment with deep learning models (LSTM/GRU) for time series sensors  
- Integrate monitoring dashboard for live fault detection
