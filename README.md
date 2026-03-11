# 📊 Skillytics – Calculus Performance Prediction System

## 📌 Overview

A **machine learning-based prediction system** designed to analyze student data in order to predict their performance in **Calculus-related subjects**.

The system processes raw student datasets, performs data cleaning and preprocessing, and applies machine learning techniques to identify patterns that influence calculus learning outcomes.

By analyzing these patterns, the system helps identify students who may require additional support in calculus.

---

## ❗ Problem Statement

Calculus is one of the most challenging subjects for many students, and educators often struggle to identify struggling students early.

Without proper data analysis, it becomes difficult to determine:

* Which students may struggle with calculus
* What factors influence calculus performance
* How academic and technical skills affect calculus learning

This project addresses this issue by applying **machine learning techniques** to analyze student data and predict calculus performance.

---

## 🧠 Machine Learning Approach

The project uses **K-Nearest Neighbors (KNN)** to predict student calculus performance.

### Model Workflow

1. Load student dataset
2. Perform data cleaning and preprocessing
3. Encode categorical variables using **Label Encoding**
4. Split dataset into training and testing sets
5. Train prediction model using **KNN classifier**
6. Evaluate model performance using accuracy metrics
7. Validate model using **K-Fold Cross Validation**

---

## ✨ Key Features

* 📊 Student dataset analysis for calculus performance
* 🧹 Data preprocessing and cleaning
* 🔄 Label encoding for categorical variables
* 🤖 Machine learning prediction using **KNN**
* 🔬 Model evaluation using **accuracy and confusion matrix**
* 📉 Data visualization using **Matplotlib and Seaborn**

---

## 🛠️ Tech Stack

### 💻 Programming Language

Python

### 📚 Libraries

* Pandas
* Scikit-learn
* Matplotlib
* Seaborn
* NumPy

### 🔧 Tools

* Jupyter Notebook
* Git
* GitHub

---

## 📁 Project Structure

```
Skillytics/
│
├── data/                         # Student dataset
│
├── calculus-prediction.ipynb     # Main machine learning notebook
│
├── README.md                     # Project documentation
```

---

## 🔄 Machine Learning Pipeline

1️⃣ Load the raw student dataset
2️⃣ Perform data cleaning and preprocessing
3️⃣ Encode categorical variables using **LabelEncoder**
4️⃣ Prepare feature variables and target variable
5️⃣ Train the prediction model using **KNN classifier**
6️⃣ Validate the model using **K-Fold Cross Validation**
7️⃣ Evaluate prediction performance using accuracy metrics

---

## 🚀 Installation

Clone the repository

```
git clone https://github.com/aqimxn/skillytics.git
cd skillytics
```

Run the notebook

```
jupyter notebook
```

---

## 📊 Learning Outcomes

This project demonstrates:

* Data preprocessing using **Pandas**
* Machine learning classification using **KNN**
* Model evaluation using **Scikit-learn**
* Data visualization using **Matplotlib and Seaborn**
* Machine learning workflow development

---

## 🔮 Future Improvements

* 📈 Test additional machine learning models (Random Forest, SVM)
* 📊 Build a web dashboard for prediction results
* 🌐 Deploy the prediction model as an API
* ☁️ Deploy the system on cloud platforms

---

## 👨‍💻 Author

**Muhammad Aqiman**

GitHub: https://github.com/aqimxn