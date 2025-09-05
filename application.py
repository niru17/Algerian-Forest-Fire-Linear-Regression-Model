from flask import Flask, jsonify, render_template, request
import pickle
import pandas as pd
import numpy as np

application=Flask(__name__)
app=application

## Import ridge and scaler pickles
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/prediction_data",methods=['GET','POST'])
def predict_datapoint():
    if request.method=="POST":
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        WS = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))
        
        new_standard_scaler=standard_scaler.transform([[Temperature,RH,WS,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_standard_scaler)
        return render_template('home.html',result=result[0])
    else:
        return render_template('home.html')
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5002)