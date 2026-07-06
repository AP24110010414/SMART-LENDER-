from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load models
with open('rdf.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scale1.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extract features from form
            gender = int(request.form['gender'])
            married = int(request.form['married'])
            dependents = int(request.form['dependents'])
            education = int(request.form['education'])
            self_employed = int(request.form['self_employed'])
            applicant_income = float(request.form['applicant_income'])
            coapplicant_income = float(request.form['coapplicant_income'])
            loan_amount = float(request.form['loan_amount'])
            loan_amount_term = float(request.form['loan_amount_term'])
            credit_history = float(request.form['credit_history'])
            property_area = int(request.form['property_area'])

            # Create numpy array
            features = np.array([[gender, married, dependents, education, self_employed,
                                  applicant_income, coapplicant_income, loan_amount,
                                  loan_amount_term, credit_history, property_area]])

            # Scale features
            scaled_features = scaler.transform(features)

            # Predict
            prediction = model.predict(scaled_features)
            
            result = "Approved" if prediction[0] == 1 else "Rejected"
            
            return render_template('result.html', prediction_text=f'Loan {result}', result_type=result)
        
        except Exception as e:
            return render_template('result.html', prediction_text=f'Error: {str(e)}', result_type='Error')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
