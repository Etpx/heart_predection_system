# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import json
import pandas as pd

# Access Flask
app = Flask(__name__)

# Open the model
model = pickle.load(open('model.pkl', 'rb'))

# Load the html page on home route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    possible_disease = []
    message = ""

    if output:
        output = "The patient has a disease!"
        message = "The major causes of the disease are:"
    else:
        output = "The patient doesn't have a disease!"
        message = "But.. be careful of the following factors!"

    if (int(request.form["trestbps"])) > 120:
        possible_disease.append("Blood pressure")

    if (int(request.form["chol"])) > 130:
        possible_disease.append("Cholesterol")

    if (int(request.form["fbs"])) >= 1:
         possible_disease.append("Fasting blood sugar")

    if (int(request.form["thalach"])) > 100:
        possible_disease.append("Heart rate")

    if (float(request.form["oldpeak"])) > 1.0:
        possible_disease.append("ST depression induced by exercise relative to rest")

    if (int(request.form["ca"])) >= 1:
        possible_disease.append("Major Vessels")

    if (int(request.form["thal"])) >= 2:
        possible_disease.append("thalassemia")

    print(possible_disease)

    return render_template('index.html', prediction_text=output, possible_disease=possible_disease, message=message)

if __name__ == "__main__":
    app.run(debug=True)
