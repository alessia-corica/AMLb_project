# Breast Cancer Diagnosis with Machine Learning

---

## Table of Contents

- [Project Background and Objectives](#project-background-and-objectives)
- [Dataset](#dataset)
- [Repository Structure](#repository-structure)
- [Machine Learning Workflow](#machine-learning-workflow)
- [Software and Libraries](#software-and-libraries)
- [Model Performance Summary](#model-performance-summary)

---

## Project background and Objectives

This project looks at how supervised machine learning can be used to classify breast tumors as benign or malignant using the **Breast Cancer Wisconsin Diagnostic dataset**.

The goal is to compare different classification models, in particular **Logistic Regression, Support Vector Machine (SVM), Linear Discriminant Analysis (LDA), and K-Nearest Neighbors (KNN)**, within the same workflow. This allows to understand how their predictions differ and how these differences may affect their reliability, especially in a medical setting.

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
```
├── data/  
│   ├── raw/  
│   └── processed/  
├── notebooks/  
├── plots/  
├── results/  
├── scripts/  
├── LICENSE  
└── README.md
```

### `data/`
Contains the datasets used in the project.

- **raw/**: original dataset.  
- **processed/**: preprocessed dataset split into input features and target labels, further divided into training and test sets used for model training and evaluation.

### `notebook/`
Jupyter notebook containing the full machine learning workflow, including exploratory analysis (EDA), preprocessing, model training, and evaluation.

### `plots/`
This directory contains all plots generated during the analysis.  
It includes plots used for EDA (such as feature distributions, boxplots, and correlation matrix) as well as plots used for model evaluation and comparison, including confusion matrices, ROC curves, and precision–recall curves.

### `results/`
Table containing the evaluation metrics of the trained models, including Accuracy, Precision, Recall, F1 score, ROC-AUC, and Average Precision on the test set.

### `scripts/`
This folder contains utility scripts used in the project.  
In particular, it includes `saving.py`, which provides helper functions used in the notebook to save plots, results, and other outputs generated during the analysis.

### `LICENSE`
License file specifying how the contents of the repository can be used.

### `README.md`
Main documentation file describing the project and its structure.

---
## Machine Learning Workflow

The machine learning pipeline implemented in this project consists of the following steps:

1. **Data Loading**  
   Import the Breast Cancer Wisconsin Diagnostic Dataset directly from the UCI Machine Learning Repository.

2. **Exploratory Data Analysis (EDA)**  
   Inspect class distribution, visualize feature distributions by diagnosis class, and compute a Pearson correlation matrix to identify potential multicollinearity among predictors.

3. **Train/Test Split**  
   Partition the dataset into training and test sets (70/30) using stratified sampling to preserve class proportions.

4. **Model Training**  
   Train four supervised classifiers within a consistent pipeline (StandardScaler + SelectKBest + model):
   - Logistic Regression
   - Support Vector Machine (RBF kernel)
   - Linear Discriminant Analysis (LDA)
   - K-Nearest Neighbors (KNN)

5. **Hyperparameter Tuning**  
   Optimize model configurations using GridSearchCV with 5-fold stratified cross-validation, tuning both model hyperparameters and the number of selected features (SelectKBest).

6. **Model Evaluation**  
   Evaluate model performance on the test set using accuracy, precision, recall, F1-score, ROC-AUC, and Average Precision. Models are compared using ROC and Precision–Recall curves.
   
---
## Software and Libraries

The following Python libraries were used for data analysis, visualization, and machine learning:

- **NumPy** – numerical computing
- **Pandas** – data manipulation and tabular data processing
- **Matplotlib** – data visualization
- **Seaborn** – statistical data visualization
- **Scikit-learn** – machine learning algorithms, model evaluation, and feature selection
  - `Pipeline`, `StandardScaler`, `SelectKBest`
  - `LogisticRegression`, `SVC`, `LinearDiscriminantAnalysis`, `KNeighborsClassifier`
  - `GridSearchCV`, `train_test_split`, `StratifiedKFold`
  - Metrics: `accuracy_score`, `f1_score`, `roc_auc_score`, `average_precision_score`, and more
---
## Model Performance Summary

The predictive performance of the classifiers was evaluated on an independent test set using standard classification metrics.

| Model | Accuracy | Precision | Recall | F1-score |
|-------|----------|-----------|--------|----------|
| Logistic Regression | 0.977 | 0.984 | 0.953 | 0.968 |
| SVM (RBF kernel) | 0.994 | 1.000 | 0.984 | 0.992 |
| LDA | 0.953 | 1.000 | 0.875 | 0.933 |
| KNN | 0.959 | 0.983 | 0.906 | 0.943 |

All models achieved high predictive performance, with accuracy values above 0.95 and **ROC-AUC values close to 1**, indicating excellent separability between benign and malignant samples.

**Logistic Regression** achieved strong and well-balanced results, with good precision and recall despite being the simplest model in the comparison. **SVM with RBF kernel** achieved the best overall performance, with the highest F1-score (0.992) and perfect precision. **LDA** showed the lowest recall (0.875), indicating a higher tendency to miss some malignant cases at the default threshold. **KNN** achieved solid results, although with slightly lower recall compared to Logistic Regression and SVM.

