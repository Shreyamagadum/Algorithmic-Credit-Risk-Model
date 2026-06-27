# Algorithmic-Credit-Risk-Model

## 💳 Credit Risk Prediction using ElasticNet

## 🚀 Live Demo:
https://algorithmic-credit-risk-model-gcdi99mpn2vgobyc7ajhke.streamlit.app

## 📌 Project Overview
This project focuses on building an **algorithmic credit risk model** to predict the probability of loan default for applicants applying for high-value loans.

The model uses **ElasticNet regularization** combined with robust preprocessing techniques such as outlier removal and SMOTE to handle class imbalance.

---

## 🎯 Objective
To develop a machine learning model that can:
- Predict whether a borrower will default on a loan
- Output a **probability of default**
- Improve decision-making in credit risk assessment

---

## 📂 Dataset Description
The dataset contains borrower-level financial and demographic information such as:
- Age
- Income
- Loan amount
- Loan intent
- Credit grade
- Previous default history

**Target Variable:**
- `loan_status`
  - `0` → No Default  
  - `1` → Default  

---

## ⚙️ Workflow

### 1. Exploratory Data Analysis (EDA)
- Checked dataset structure and summary statistics
- Identified missing values and feature distributions

### 2. Data Cleaning
- Handled missing values using mean imputation
- Converted categorical variables into numerical format using one-hot encoding

### 3. Outlier Removal
- Removed extreme values using **Z-score method (3 standard deviations)**

### 4. Handling Imbalanced Data
- Applied **SMOTE (Synthetic Minority Oversampling Technique)** to balance target classes

### 5. Feature Scaling
- Standardized features using **StandardScaler** for better model performance

### 6. Model Training
- Trained a **Logistic Regression model with ElasticNet regularization**
- Combined L1 and L2 penalties for stability and feature selection

### 7. Model Evaluation
- Evaluated performance using **ROC-AUC score**
- Visualized model performance using ROC Curve

---

## 📈 Results

- **Baseline ROC-AUC Score:** 0.74  
- **Improved ROC-AUC (after scaling & tuning):** ~0.76–0.80  

👉 The model demonstrates good predictive capability for distinguishing between defaulters and non-defaulters.

---

## 🧠 Key Learnings

- Handling imbalanced datasets significantly improves model performance
- Feature scaling is crucial for regularized models like ElasticNet
- Outlier removal helps stabilize predictions
- ROC-AUC is an effective metric for classification problems in finance

---

## 🛠️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Imbalanced-learn (SMOTE)  
- Matplotlib, Seaborn

---

## 🚀 How to Run

1. Clone the repository
```bash
https://github.com/Shreyamagadum/Algorithmic-Credit-Risk-Model
```

2. Open Jupyter Notebook
    jupyter lab
   
3. Run all cells in:
    credit_risk_model.ipynb

---
## Output
# Dashboard
<img width="1913" height="911" alt="Image" src="https://github.com/user-attachments/assets/16ee2ac2-e22c-42aa-9ed2-7af3bb1d00fc" />
# Input fields
<img width="1917" height="911" alt="Image" src="https://github.com/user-attachments/assets/60e085ad-e51a-400e-bd93-135f8c5b2f5f" />
# Prediction
<img width="1915" height="915" alt="Image" src="https://github.com/user-attachments/assets/8561fc31-2202-40b9-b12f-e091d71bed71" />
# Application Summary
<img width="1905" height="908" alt="Image" src="https://github.com/user-attachments/assets/52ab299c-bbaa-4ba0-8629-b07985b3ed57" />

## 📌 Future Improvements

 - Hyperparameter tuning using GridSearchCV
 - Feature importance analysis
 - Deployment using Streamlit (UI)
 - Integration with real-time loan application systems

---


## 👨‍💻 Author

- Shreya Magadum

---

## ⭐ Acknowledgment
- This project was developed as part of a machine learning assignment focused on credit risk modeling using ElasticNet, SMOTE, and ROC-AUC evaluation.
---

