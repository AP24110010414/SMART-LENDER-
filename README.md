# SMART LENDER

## Overview

SMART LENDER is an AI-powered loan approval prediction system that helps financial institutions evaluate loan applications efficiently. The application uses Machine Learning algorithms to predict whether a loan should be approved based on applicant details, reducing manual effort and improving decision-making.

---

## Features

- Loan eligibility prediction using Machine Learning
- User-friendly Flask web application
- Real-time prediction results
- Data preprocessing and model training
- Multiple ML model comparison
- Easy deployment and scalability

---

## Project Structure

```
SMART-LENDER
│
├── Dataset/
│   └── Loan dataset used for training and testing
│
├── Training/
│   ├── Data preprocessing
│   ├── Exploratory Data Analysis
│   ├── Feature Engineering
│   ├── Model Training
│   └── Model Evaluation
│
├── Flask/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   ├── model/
│   └── requirements.txt
│
├── SMART LENDER Documentation/
│   ├── Project Report
│   ├── Architecture
│   ├── Testing Documents
│   ├── Design Documents
│   └── Other Supporting Documents
│
├── .gitignore
├── DEMO VIDEO.md
└── README.md
```

---

## Technologies Used

### Programming Languages
- Python
- HTML
- CSS
- JavaScript

### Frameworks
- Flask

### Machine Learning
- Scikit-learn
- XGBoost
- Random Forest
- Decision Tree
- K-Nearest Neighbors (KNN)

### Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Pickle

---

## Workflow

1. Collect loan applicant dataset.
2. Perform data preprocessing.
3. Analyze and visualize data.
4. Train multiple machine learning models.
5. Evaluate model performance.
6. Save the best-performing model.
7. Deploy using Flask.
8. Predict loan approval in real time.

---

## Input Parameters

The prediction is based on applicant information such as:

- Gender
- Marital Status
- Education
- Employment Status
- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

---

## Output

The system predicts one of the following:

- Loan Approved
- Loan Rejected

---

## Installation

Clone the repository

```bash
git clone https://github.com/AP24110010414/SMART-LENDER-.git
```

Move into the project directory

```bash
cd SMART-LENDER-
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app1.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## Future Enhancements

- User authentication
- Database integration
- Cloud deployment
- Advanced credit risk analysis
- Explainable AI predictions
- Loan recommendation system

---

## Documentation

The repository includes complete project documentation covering:

- Problem Statement
- Proposed Solution
- Requirement Analysis
- System Design
- Architecture
- Testing
- Results
- User Manual
- Performance Analysis

---

## Demo

Refer to **DEMO VIDEO.md** for the project demonstration.

---

## Team lead

- J. Thanuja

## Members
- Karumuru Sai Lakshmi Ruchitha
- Surya Chinta

---

## License

This project is developed for academic and educational purposes.

---

## Acknowledgements

- IBM SkillsBuild
- SRM University–AP
- Scikit-learn
- Flask
- XGBoost
