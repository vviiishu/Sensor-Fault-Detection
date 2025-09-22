# Sensor Fault Detection

## Project Overview

This project implements a machine learning pipeline for detecting faults in sensor data. Faulty sensors can produce misleading information that impacts system reliability, safety, and efficiency. The system automates data ingestion, preprocessing, model training, and prediction to identify anomalies or faults in real time or from historical data. It is designed to be modular, reproducible, and deployment-ready.

## Features

* Data Ingestion: Load and preprocess raw sensor data for training and inference.
* Modular Pipeline: Config-driven workflow for training, evaluation, and prediction.
* Fault Detection: Classifies or detects anomalies in sensor readings.
* Model Persistence: Saves trained models for future use.
* Logging & Error Handling: Ensures reliability and traceability.
* Deployment Ready: Supports integration with APIs or dashboards.

## Tech Stack

* Language: Python  
* Machine Learning: scikit-learn, pandas, numpy  
* Visualization: matplotlib, seaborn  
* Model Persistence: pickle / joblib  
* Deployment: Flask / FastAPI (if enabled)

## Project Structure

