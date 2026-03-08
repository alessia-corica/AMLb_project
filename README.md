# Breast Cancer Diagnosis with Machine Learning

---

## Table of Contents

- [Project Background and Objectives](#project-background-and-objectives)
- [Dataset](#dataset)
- [Repository Structure](#repository-structure)
- [Machine Learning Workflow](#machine-learning-workflow)
- [Software and Libraries](#software-and-libraries)
- [Model Performance Summary](#model-performance-summary)
- [References](#references)

---

## Project background and Objectives
This project implements a supervised machine learning pipeline to classify breast tumors as **benign** or **malignant** using the **Breast Cancer Wisconsin Diagnostic Dataset**. The objective is to evaluate the performance of two widely used classifiers, **Logistic Regression** and **Support Vector Machine (SVM)**, within a structured workflow including preprocessing, model training, and performance evaluation.

The project also addresses several practical challenges commonly encountered in biomedical classification tasks, such as **class imbalance** and **correlations among predictors**, that can influence the reliability and interpretability of model predictions.

---
## Dataset

The analysis uses the **Breast Cancer Wisconsin Diagnostic Dataset**, available from the **UCI Machine Learning Repository**:

https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)

Dataset characteristics:

- **569 samples** representing breast tumor cases
- **30 numerical features** describing morphological properties of cell nuclei extracted from **fine needle aspirate (FNA) images**
- Features include measurements such as **radius, texture, perimeter, area, smoothness, concavity, and symmetry**
- **Target variable:** tumor diagnosis (**Benign** or **Malignant**)
- **Machine learning task:** binary classification

---
## Repository Structure
---
## Machine Learning Workflow

## Machine Learning Workflow

The machine learning pipeline implemented in this project consists of the following steps:

1. **Data Loading**  
   Import the Breast Cancer Wisconsin Diagnostic Dataset into the project environment.

2. **Exploratory Data Analysis (EDA)**  
   Inspect class distribution, visualize feature relationships, and compute a Pearson correlation matrix to identify potential multicollinearity.

3. **Preprocessing**  
   - Encode the diagnostic labels using `LabelEncoder`
   - Standardize numerical features using `StandardScaler`

4. **Train–Test Split**  
   Partition the dataset into training and test sets (80/20) using stratified sampling.

5. **Model Training**  
   Train two supervised classifiers:
   - Logistic Regression  
   - Support Vector Machine (RBF kernel)

6. **Cross-Validation**  
   Apply **Stratified 5-Fold Cross-Validation** to evaluate model robustness.

7. **Model Evaluation**  
   Evaluate model performance on the test set using standard classification metrics and diagnostic curves.
   
---
## Software and Libraries
---
## Model Performance Summary
---
## References
