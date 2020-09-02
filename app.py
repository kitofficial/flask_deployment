# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 16:41:28 2020

@author: Ankit
"""

from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
model = pickle.load(open('area_price.pkl', 'rb'))
import numpy as np


from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')  
def about():
    return render_template('about.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features=[]
    for x in request.form.values():
        try:
            convert=int(x)
            int_features.append(convert)
        except:
            print("Its string")


    #int_features=int_features[1:len(int_features)]
    #int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    #predicted=output


    return render_template('index.html', 
        prediction_text='price is ={}'.format(output)
        )

if __name__ == "__main__":
	app.run(debug=True)