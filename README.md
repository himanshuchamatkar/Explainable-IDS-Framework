# 🔐 AI Powered Realtime Intrusion Detection System

An **Explainable AI-based Intrusion Detection System (IDS)** designed to detect malicious network activity using machine learning and visualize security insights through an interactive dashboard.

This project analyzes network traffic flows and classifies them as **BENIGN or ATTACK** while also providing **explainable AI insights using SHAP**.

---

## 🚀 Live Dashboard

Streamlit App

explainable-ids-framework ∙ main ∙ dashboard/app.py




---

## 📌 Features

* Real-time network traffic monitoring dashboard
* Machine Learning based attack detection
* Explainable AI using **SHAP feature importance**
* Attack probability visualization
* Threat level monitoring
* Top attacker IP identification
* Protocol distribution analysis
* Live alert monitoring

---

## 🧠 Machine Learning Models

Two models were trained for intrusion detection:

* Random Forest Classifier
* XGBoost Classifier

Both models were trained on the **CICIDS2017 dataset**.

---

## 📊 Dataset

Dataset used:

**CICIDS2017 Network Intrusion Dataset**

It contains multiple attack categories including:

* DDoS
* PortScan
* Brute Force
* Web Attacks
* Infiltration

For this project the dataset was simplified into **binary classification**:

* BENIGN
* ATTACK

---

## 🧩 Project Architecture

Network Traffic
↓
Feature Extraction
↓
Machine Learning Model (RF / XGBoost)
↓
Prediction + Probability
↓
SHAP Explainability
↓
Streamlit Security Dashboard

---

## 📁 Project Structure

```
Explainable-IDS-Framework
│
├── dashboard
│   ├── app.py
│   └── sample_predictions.json
│
├── src
│   ├── data_preprocessing
│   ├── models
│   ├── training
│   ├── realtime
│   ├── evaluation
│   └── explainability
│
├── prepare_dataset.py
├── train_random_forest.py
├── train_xgboost.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/himanshuchamatkar/Explainable-IDS-Framework.git
cd Explainable-IDS-Framework
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Dashboard

```bash
streamlit run dashboard/app.py
```

Open browser:

```
http://localhost:8501
```

---

## 📊 Dashboard Capabilities

The dashboard provides:

* Total network flows
* Attack alerts
* Benign traffic monitoring
* Attack probability timeline
* Traffic classification distribution
* Top suspicious IPs
* Protocol distribution
* Live alert logs
* SHAP explainability for predictions

---

## 🔍 Explainable AI

To make the IDS more transparent, **SHAP values** are used to explain the contribution of each feature to the model's prediction.

This helps security analysts understand **why a particular traffic flow was flagged as malicious**.

---

## 🛠 Technologies Used

* Python
* Streamlit
* Scikit-Learn
* XGBoost
* SHAP
* Pandas
* Plotly
* CICIDS2017 Dataset

---

## 🎓 Academic Context

This project was developed as part of a **Cybersecurity and Machine Learning research project** focusing on **Explainable Intrusion Detection Systems**.

---

## 👨‍💻 Author

Himanshu Vikas Chamatkar
B.Tech Computer Science Engineering
DMIMS Wardha

GitHub:
https://github.com/himanshuchamatkar

---

## ⭐ If you found this project useful, consider giving it a star.
