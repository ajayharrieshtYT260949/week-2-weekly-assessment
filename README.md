# Week 2 - Weekly Assessment

## Machine Learning

**Duration:** 1 Day (Approximately 6 Hours)  
**Mode:** Individual Hands-on Assessment

## Project Overview

This project implements an end-to-end Machine Learning workflow for a banking use case.

The bank aims to:

1. Predict whether a loan applicant is likely to default.
2. Estimate the loan amount requested by a customer.
3. Segment customers based on their characteristics using clustering.

The project covers data preprocessing, feature engineering, model training, evaluation, hyperparameter tuning, and customer segmentation.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Jupyter Notebook
- Joblib
- Git and GitHub

## Project Structure

```text
week-2-weekly-assessment/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│
├── models/
│
├── reports/
│   └── figures/
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Assessment Tasks

### Task 1 - Concepts, Splits and Leakage

- Train, validation and test splitting
- Decision Tree overfitting demonstration
- Logistic Regression cross-validation
- Data leakage demonstration
- Supervised and unsupervised learning concepts

### Task 2 - Preprocessing, Features and Pipeline

- Missing value imputation
- Categorical encoding
- Feature engineering
- Feature scaling
- ColumnTransformer and Pipeline
- Model serialization using Joblib

### Task 3 - Models: Supervised and Unsupervised

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- Linear Regression
- Ridge and Lasso
- K-Means clustering

### Task 4 - Evaluation and Tuning

- Classification evaluation metrics
- Confusion matrix
- ROC curve and ROC-AUC
- Decision threshold optimization
- GridSearchCV
- RandomizedSearchCV
- Regression evaluation metrics
- Final test-set evaluation

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/ajayharrieshtYT260949/week-2-weekly-assessment.git
```

Navigate to the project:

```bash
cd week-2-weekly-assessment
```

Create a virtual environment:

```bash
py -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Dataset

The dataset will be provided by the trainer.

Original data will be stored in `data/raw/`, while processed data will be stored in `data/processed/`.

## Results

Model performance, evaluation metrics, visualizations, and findings will be documented after completing the assessment.

## Task 4 — Model Evaluation and Hyperparameter Tuning

### Classification Evaluation
- Evaluated Logistic Regression, Random Forest, and XGBoost.
- Calculated accuracy, precision, recall, F1-score, and ROC-AUC.
- Generated confusion matrices and ROC curves.
- Selected a classification threshold using validation data to achieve at least 75% recall.

### Hyperparameter Tuning
- Used `GridSearchCV` with three hyperparameters to tune the Random Forest classifier.
- Used `RandomizedSearchCV` with 15 parameter combinations to tune XGBoost.
- Compared the tuned models using validation metrics.

### Regression Evaluation
- Evaluated Linear Regression, Ridge Regression, and Lasso Regression.
- Compared MAE, RMSE, and R² against a mean-prediction baseline.
- Selected the best regression model using validation RMSE.

### Final Evaluation
- Evaluated the selected classification and regression models on the untouched test set.
- Saved the selected models, classification threshold, evaluation reports, and figures.

### Outputs
- `reports/task4_initial_classification_results.csv`
- `reports/task4_tuned_classification_results.csv`
- `reports/task4_random_forest_search_results.csv`
- `reports/task4_xgboost_search_results.csv`
- `reports/task4_regression_results.csv`
- `reports/task4_final_classification_test.csv`
- `reports/task4_final_regression_test.csv`
- `reports/figures/` — Task 4 evaluation plots
- `models/` — Selected classification and regression models

## Author

Ajay Harriesh T.

## Project Status

Repository and development environment setup completed. ML implementation is pending dataset availability.