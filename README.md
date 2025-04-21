# Data Driven Insights for Exception Prediction in Transport Order Management


This project tackles a real-world challenge in supply chain logistics: predicting volume-related exceptions in transport orders **before they happen**. By combining historical transport data with machine learning, the solution helps prevent disruptions, reduce manual coordination, and improve delivery reliability.

---

## 📌 Project Objective

Suppliers typically submit transport orders a day before pickup, including details like shipment volume, weight, and number of pallets. However, deviations on the day of pickup—such as shipping more or less than expected—are common. These **exceptions** can:

- Disrupt the entire transport process
- Increase operational workload
- Lead to issues in downstream production lines

The goal is to build a predictive model that identifies high-risk transport orders **in advance**, allowing for timely intervention and mitigation.

---

## 📊 Dataset Overview

The dataset used contains historical transport order records with attributes such as:

- Shipment features: `Volume`, `Gross_weight`, `Loading_meter`, etc.
- Route information: `Consignor_country`, `Recipient_country`
- Exception history: flags for prior exceptions
- Target label:  
  - `RED` = Volume exception occurred  
  - `GOOD` = No exception occurred

---

## 🧹 Data Preparation & Feature Engineering

Steps followed:
- Loaded and explored the dataset
- Cleaned irrelevant and duplicate data
- Handled missing values
- Encoded categorical columns into numerical format
- Performed feature correlation analysis
- Selected relevant features for modeling

---

## 🤖 Machine Learning Model

Model used: **Random Forest Classifier**

### 🔍 Feature Selection
Top 10 features selected based on importance:
- `Loading_meter`
- `Gross_weight`
- `Volume`
- `Handling_unit_quantity`
- `Billed_freight_weight`
- `Consignor_country`
- `Recipient_country`
- `Exception_1_week_ago`
- `Exception_2_weeks_ago`
- `Distance_cluster`

### ✅ Why Random Forest?
- Handles high-dimensional and missing data
- Doesn’t require feature scaling
- Prevents overfitting using bagging
- Provides built-in feature importance

---

## 📈 Model Evaluation

Two versions of the model were tested:
- Trained on **25 features** (full set)
- Trained on **10 selected features**

The final model was chosen based on **precision-focused** performance. A **precision greater than 65%** was achieved, aligning with the project’s target.

---

## 🖥️ Graphical User Interface (GUI)

To make the solution accessible to non-technical users, a **graphical user interface** was developed.

**Features:**
- Input transport order data manually or via file
- Get real-time predictions
- View exception risk directly in the app

---

## 🧰 Tech Stack

- **Language**: Python  
- **ML Libraries**: `scikit-learn`, `pandas`, `matplotlib`, `seaborn`  
- **GUI**: `Tkinter` or `PyQt`  
- **Notebook**: Jupyter

---

## 📦 Project Structure

