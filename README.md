# 🏦 Banking Fraud Detection System Using Machine Learning

## 📌 Project Overview

The Banking Fraud Detection System is a Machine Learning-based application designed to detect fraudulent banking transactions. The project uses the Credit Card Fraud Detection dataset and a Random Forest Classifier to classify transactions as either genuine or fraudulent.

The system includes an interactive Streamlit dashboard with employee login authentication, fraud analytics, transaction verification, and simulated email/SMS fraud alerts.

---

## 🚀 Features

* 🔐 Bank Employee Login System
* 🤖 Machine Learning-Based Fraud Detection
* 📊 Interactive Data Visualization Dashboard
* 📈 Fraud vs Genuine Transaction Analysis
* 🥧 Fraud Percentage Pie Chart
* 🚨 Fraud Alert Simulation
* 📧 Email Alert Simulation
* 📱 SMS Alert Simulation
* 💾 Saved Trained Model (`fraud_model.pkl`)
* 🌐 Streamlit Web Application

---

## 🛠 Technologies Used

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Programming Language      |
| Pandas        | Data Processing           |
| Scikit-Learn  | Machine Learning          |
| Random Forest | Fraud Detection Algorithm |
| Matplotlib    | Data Visualization        |
| Streamlit     | Web Dashboard             |
| Joblib        | Model Saving & Loading    |
| VS Code       | Development Environment   |

---

## 📂 Project Structure

```text
Banking-Fraud-Detection/
│
├── app.py
├── main.py
├── predict.py
├── fraud_model.pkl
├── creditcard.csv
├── requirements.txt
└── README.md
```

---



## 🧠 Machine Learning Algorithm

### Random Forest Classifier

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

### Why Random Forest?

* High Accuracy
* Robust Performance
* Handles Large Datasets
* Works Well for Classification Problems

---


## 🚨 Alert Simulation

When a fraudulent transaction is detected, the system can simulate:

### Email Alert

```text
To: fraud@bank.com

Subject: Fraud Transaction Alert

A suspicious transaction has been detected.
Immediate verification is required.
```

### SMS Alert

```text
WARNING!

Fraudulent transaction detected.

Account temporarily flagged.

Please contact the bank immediately.
```

---

## ▶️ Installation

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🔑 Demo Login Credentials

```text
Employee ID: admin
Password: bank123
```

---

## 🔮 Future Scope

* Real-Time Fraud Monitoring
* SMTP Email Integration
* SMS Integration using Twilio API
* Multi-User Authentication
* Database Connectivity
* Banking API Integration
* Deep Learning-Based Fraud Detection
* Cloud Deployment

