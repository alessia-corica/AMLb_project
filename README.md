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

The repository is organized to keep data, code, results, and documentation clearly separated, ensuring reproducibility and readability of the project.

├── data/  
│   ├── raw/  
│   └── processed/  
├── notebooks/  
├── plots/  
├── results/  
├── scripts/  
├── LICENSE  
└── README.md

### data/
Contains the datasets used in the project.

- **raw/**: original dataset.  
- **processed/**: cleaned and preprocessed data used for model training and evaluation.

### notebooks/
Jupyter notebooks containing the full machine learning workflow, including exploratory analysis, preprocessing, model training, and evaluation.

### plots/
This directory contains all plots generated during the analysis.  
It includes plots used for exploratory data analysis (such as feature distributions, boxplots, and correlation matrices) as well as plots used for model evaluation and comparison, including confusion matrices, ROC curves, and precision–recall curves.

### results/
Tables containing the evaluation metrics of the trained models.  
This folder includes the performance results for Logistic Regression and SVM, as well as a comparison table summarizing the metrics of both models.

### scripts/
This folder contains utility scripts used in the project.  
In particular, it includes `saving.py`, which provides helper functions used in the notebooks to save plots, results, and other outputs generated during the analysis.

### LICENSE
License file specifying how the contents of the repository can be used.

### README.md
Main documentation file describing the project and its structure.

---
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

The following Python libraries were used for data analysis, visualization, and machine learning:

- **NumPy** – numerical computing
- **Pandas** – data manipulation and tabular data processing
- **Matplotlib** – data visualization
- **Seaborn** – statistical data visualization
- **Scikit-learn** – machine learning algorithms and model evaluation

---
## Model Performance Summary

The predictive performance of the classifiers was evaluated on an independent test set using standard classification metrics.

| Model | Accuracy | Precision | Recall | F1-score |
|------|------|------|------|------|
| Logistic Regression | 0.977 | 0.984 | 0.953 | 0.968 |
| SVM (RBF kernel) | 0.982 | 0.984 | 0.969 | 0.976 |

Logistic Regression was selected as a **baseline linear classifier**, providing interpretable probabilistic predictions. The Support Vector Machine with **RBF kernel** was included as a more flexible model capable of capturing **non-linear relationships among predictors**.

Both models achieved very high predictive performance, with **ROC-AUC values close to 1**, indicating excellent separability between benign and malignant samples. The SVM model slightly improved recall for the malignant class, reducing the number of false negatives.

---
## References
