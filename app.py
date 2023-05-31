from flask import Flask, request,render_template, jsonify
import pickle
from logging import debug
import utils  
from utils import preprocessdata 

app = Flask(__name__) 
pickle_in=open('rfc.pkl','rb')
rfc=pickle.load(pickle_in)

@app.route('/') 
def home(): 
    return render_template('index.html') 
@app.route('/predict/', methods=['GET', 'POST'])

def predict():  
        if request.method == 'POST': 
            print(request.form)  # check the data submitted by the form
            loan_amount = request.form.get('Current Loan Amount')
            credit_score = '1000'
            annual_income = request.form.get('Annual Income')
            monthly_debt = '1400'
            print(loan_amount, credit_score, annual_income, monthly_debt)  # check the values of the variables
            # ... rest of the code
        else:
            print(request.method)  # check the req

        if not loan_amount or not credit_score or not annual_income or not monthly_debt:
            return "Input values cannot be empty"

        # Pass input values to preprocessdata() function for further validation
        prediction = utils.preprocessdata(loan_amount, credit_score, annual_income, monthly_debt)

        if prediction == "Invalid input values":
            return "Invalid input values"
        elif prediction == "Input values cannot be negative":
            return "Input values cannot be negative"
        elif prediction == "Input values are too large":
            return "Input values are too large"
        return render_template('predict.html', prediction=prediction)

if __name__ == '__main__': 
    app.run(port=5002) 
