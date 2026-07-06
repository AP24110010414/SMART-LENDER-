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

_Add a screenshot here._

### Loan Application Form

_Add a screenshot here._

### Prediction Result

_Add a screenshot here._

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

## Author

**Thanuja Jonnalagadda**

B.Tech Computer Science and Engineering  
SRM University-AP

---

## License

This project is developed for educational and academic purposes.