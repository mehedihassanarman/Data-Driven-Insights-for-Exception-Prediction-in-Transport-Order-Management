# Data Driven Insights for Exception Prediction in Transport Order Management
In modern supply chain operations, even a small disruption can ripple across the entire logistics network. This project addresses a critical issue in transport management: identifying transport orders that are likely to result in volume-related exceptions—before they happen.

By combining historical data analysis and machine learning, this project provides a predictive solution that helps reduce manual effort, avoid production delays, and optimize logistics operations.

---

## Project Objective

Every day, suppliers release transport orders with planned shipment details like pickup date, weight, volume, and number of pallets. However, real-world pickups often deviate from this plan: the supplier may ship more, less, or even fail to ship altogether. These deviations are called **exceptions**, and they:

- Interrupt the flow of goods

- Increase workload for logistics teams

- Potentially cause costly production downtimes

The goal of this project is to **predict these exceptions in advance** using machine learning, allowing companies to take preventive action.

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

