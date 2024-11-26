import os
import pandas as pd 
import numpy as np
from flask import Flask, render_template, request
from src.datasience.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/train', methods=['GET']) # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successfull!!"

@app.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            data = [
                fixed_acidity, 
                volatile_acidity, 
                citric_acid, 
                residual_sugar, 
                chlorides, 
                free_sulfur_dioxide, 
                total_sulfur_dioxide, 
                density, 
                pH, 
                sulphates, 
                alcohol
            ]

            data = np.array(data).reshape(1, 11)

            prediction_pipeline_obj = PredictionPipeline()
            predict = prediction_pipeline_obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ', e)
            return 'Something went wrong'

    else:
        return render_template('index.html')
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)