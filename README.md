

# Predictive Maintenance Project

This repository contains the implementation of a predictive maintenance system using the AI4I 2020 Predictive Maintenance Dataset. The goal of this project is to develop an MLOps pipeline that automates the machine learning workflow for predictive maintenance tasks.

## Project Overview

The project involves the following key tasks:

- Version control using Git
- Data versioning with DVC
- Experiment tracking with MLflow
- Model training and deployment with automation
- Monitoring and maintenance of the deployed model

## Dataset

The dataset used in this project is the AI4I 2020 Predictive Maintenance Dataset, which consists of multivariate time-series data with 10,000 instances and 14 features. The dataset is sourced from the UCI Machine Learning Repository and simulates real-world industry scenarios for predictive maintenance.
**Acces link:** https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset

## Repository Structure

- `data/`: Directory containing the dataset and data versioning files.
- `models/`: Trained model files and model architecture.
- `notebooks/`: Jupyter notebooks for data exploration and analysis.
- `src/`: Source code for the predictive maintenance model and utility functions.
- `requirements.txt`: Required packages for the project.

## Setup

To run the project, you need to install the necessary dependencies:

```bash
pip install -r requirements.txt
