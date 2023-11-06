# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 10:55:22 2023

@author: Aryaman Kumar
"""

#import libraries
import numpy as np
import pandas as pd 
from flask import Flask, render_template,request
import pickle#Initialize the flask App
import matplotlib.pyplot as plt 
import subprocess
from flask import Flask, render_template_string
import matplotlib.pyplot as plt, mpld3
import matplotlib
from matplotlib.figure import Figure
    
app = Flask(__name__)


#n_periods = 10
#fc, confint = model.predict(n_periods=n_periods, return_conf_int=True)

price = pd.read_csv('C:/Users/Aryaman Kumar/Desktop/DSA project/commodity_prices.csv', 
					index_col ='Year', 
					parse_dates = True)

@app.route('/')
def home():
    return render_template('index.html')
#To use the predict button in our web-app
#To use the predict button in our web-app
@app.route('/data1', methods = ['POST'])
def data1():
 
        form_data = request.form
        name=[x for x in request.form.values()]
        global cname
        cname=name[0]
        child = subprocess.Popen(['python', 'dsa4.py'], stdin=subprocess.PIPE)
        b = bytes(name[0], 'utf-8')
        child.communicate(b)
        return render_template('index.html')

@app.route('/data2', methods = ['POST'])
def data2():

        form_data = request.form
        
        time=[x for x in request.form.values()]
        len1=len(time)
        global fc
        model = pickle.load(open('model2.pkl', 'rb'))
        fc, confint = model.predict(time=time, return_conf_int=True)
        output=round(fc[int(time[0])],2)
        sum1=0
        for i in range(1,len(fc)):
            sub= fc[i]-fc[i-1]
            sum1+=sub
        if(sum1>0):
            return render_template('results.html', prediction_text='Average forecasted price for selected commodity,{}years later is {} $ per measurement unit.\n The prices show increasing trends for this period').format(time[0],output)
        if(sum1<0):
            return render_template('results.html', prediction_text='Average forecasted price for selected commodity,{}years later is {} $ per measurement unit.\n The prices show decreasing trends for this period').format(time[0],output)
        else:
            return render_template('results.html', prediction_text='Average forecasted price for selected commodity,{}years later is {} $ per measurement unit.\n The prices are stable in this period').format(time[0],output)
@app.route('/graph', methods = ['GET','POST'])
def graph():
    plt.clf ()
    plt.plot(price[cname])
    plt.title("Final Forecast of commodity price")
    plt.plot(fc, color='darkgreen',label='Inline label')
    plt.legend()
    mpld3.show()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)