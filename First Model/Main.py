# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'heart-disease-regression-model.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('main.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':

        age = int(request.form['Age'])
        sex = int(request.form.get('Sex'))
        cp = int(request.form.get('ChestPainType'))
        trestbps = int(request.form['RestingBP'])
        chol = int(request.form['Cholesterol'])
        fbs = int(request.form.get('FastingBS'))
        restecg = int(request.form['RestingECG'])
        thalach = int(request.form['MaxHR'])
        exang = int(request.form.get('ExerciseAngina'))
        oldpeak = float(request.form['Oldpeak'])
        slope = int(request.form.get('ST_Slope'))
        Kidney = int(request.form.get('KidneyDisease'))
        
        data = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,Kidney]])
        
        my_prediction = model.predict(data)
        
        return render_template('result.html', prediction=my_prediction)
        
        

if __name__ == '__main__':
	app.run(debug=True,port=8000)

