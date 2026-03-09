# Hiring Bias & Fairness Analysis (Machine Learning + Dashboard)

This project analyzes fairness in an AI-based hiring screening system.
The goal is to understand whether a machine learning model treats
candidates differently based on gender and to evaluate potential bias
using fairness metrics.

---

## Dashboard Preview
![Dashboard](assets/dashboard.png)

---

## Project Structure
hiring-bias-fairness/
├── app.py # Dash dashboard application
├── notebooks/ # EDA and ML modeling
│ └── hiring_bias_fairness_eda_model.ipynb
├── data/
│ └── raw/
│ └── resume_ai_screening.csv
├── assets/ # Dashboard screenshots
└── README.md

---

## Project Overview
Steps performed in this project:
- Exploratory Data Analysis (EDA)
- Feature encoding and preprocessing
- Training a classification model for candidate shortlisting
- Model evaluation using precision, recall, and F1-score
- Fairness analysis by gender
- Dashboard visualization using Dash

---

## Fairness Metrics Used
- **Shortlisted Rate** – how often candidates are predicted as shortlisted
- **Recall** – how many qualified candidates are correctly identified
- **False Negative Rate** – how often qualified candidates are missed

These metrics are compared across gender groups to identify disparities.

---

## Dashboard
The Dash dashboard visualizes:
- Predicted shortlisting rate by gender
- Recall by gender
- False negative rate by gender

---

## Tools & Technologies
- Python
- Pandas, NumPy
- Scikit-learn
- Dash & Plotly

---

## How to Run the Dashboard
```bash
cd hiring-bias-fairness
python app.py
