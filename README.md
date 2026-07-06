# Smart Lender

## Overview

Smart Lender is a Machine Learning-based web application that predicts whether a loan application should be approved or rejected based on applicant information. The application helps financial institutions automate the loan approval process by providing fast and data-driven predictions through a simple web interface.

---

## Features

- Loan approval prediction using Machine Learning
- User-friendly web interface
- Real-time prediction
- Data preprocessing and feature scaling
- Multiple machine learning models for comparison
- Fast and accurate decision support

---

## Tech Stack

### Programming Language
- Python

### Web Framework
- Flask

### Machine Learning
- Scikit-learn
- XGBoost

### Data Analysis
- Pandas
- NumPy

### Visualization
- Matplotlib
- Seaborn

### Frontend
- HTML
- CSS
- JavaScript

---

## Project Structure

```
SMART-LENDER/
│
├── Dataset/
│   ├── loan_prediction.csv
│   └── loan_prediction.xlsx
│
├── Flask/
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   ├── app1.py
│   ├── rdf.pkl
│   └── scale1.pkl
│
├── Training/
│   └── Loan Prediction using ML.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Dataset

The dataset contains applicant information such as:

- Gender
- Marital Status
- Dependents
- Education
- Self Employment
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

---

## Machine Learning Models

The following models were explored during development:

- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- XGBoost

The trained model is integrated with the Flask application to generate real-time loan approval predictions.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/AP24110010414/SMART-LENDER-.git
```

### Navigate to the project directory

```bash
cd SMART-LENDER
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Navigate to the Flask folder:

```bash
cd Flask
```

Run the application:

```bash
python app1.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Screenshots

### Home Page

<img width="1261" height="632" alt="image" src="https://github.com/user-attachments/assets/e4340cd4-30a3-42e9-97f3-8ebd18e00061" />

<img width="1250" height="637" alt="image" src="https://github.com/user-attachments/assets/bdfcfa00-23a9-45a2-980e-1dcd4bef205c" />

### Loan Application Form

<img width="1263" height="629" alt="image" src="https://github.com/user-attachments/assets/2d39a036-cc4f-40ac-9a87-da62bb8069ad" />

<img width="1263" height="633" alt="image" src="https://github.com/user-attachments/assets/2208d7c7-5901-4307-ad0c-d770cb2e12e9" />


### Prediction Result

<img width="1271" height="624" alt="image" src="https://github.com/user-attachments/assets/22eb0836-f1a6-4c11-a558-22d8779ad270" />


---

## Future Enhancements

- User authentication
- Database integration
- Cloud deployment
- Explainable AI for loan predictions
- Loan application history
- Admin dashboard
- Enhanced model performance

---

## Authors

**Thanuja Jonnalagadda**
**Karumuru Sai Lakshmi Ruchitha**
**Surya Vardhan Chinta**

B.Tech Computer Science and Engineering  
SRM University-AP

---

## License

This project is developed for educational and academic purposes.
