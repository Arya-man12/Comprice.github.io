# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 21:20:33 2023

@author: Aryaman Kumar
"""
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from statsmodels.tsa.seasonal import seasonal_decompose 
from statsmodels.tsa.stattools import adfuller
from numpy import log
from pandas.plotting import autocorrelation_plot
from sklearn.metrics import mean_squared_error
from math import sqrt
from pandas import DataFrame
import pmdarima as pm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import pickle
word=str(input())
price = pd.read_csv('C:/Users/Aryaman Kumar/Desktop/DSA project/commodity_prices.csv', 
					index_col ='Year', 
					parse_dates = True)

        
model = pm.auto_arima(price[word].dropna(), start_p=1, start_q=1,
                      test='adf',       # use adftest to find optimal 'd'
                      max_p=3, max_q=3, # maximum p and q
                      m=1,              # frequency of series
                      d=None,           # let model determine 'd'
                      seasonal=False,   # No Seasonality
                      start_P=0, 
                      D=0, 
                      trace=True,
                      error_action='ignore',  
                       suppress_warnings=True, 
                      stepwise=True)
print(model.summary())
        
model.plot_diagnostics(figsize=(7,5))
plt.show()
#Forecast
#n_periods = 6
#fc, confint = model.predict(n_periods=n_periods, return_conf_int=True)
#index_of_fc = np.arange(len(price[word]), len(price[word])+n_periods)

# make series for plotting purpose
#fc_series = pd.Series(fc, index=index_of_fc)
#lower_series = pd.Series(confint[:,0], index=index_of_fc)
#upper_series = pd.Series(confint[:,1], index=index_of_fc)

# Plot
#plt.plot(price[word])
#plt.plot(fc, color='darkgreen')
#plt.fill_between(lower_series.index, 
 #                lower_series, 
  #               upper_series, 
  #               color='k', alpha=.15)
#print(fc,upper_series,lower_series)
#print(fc[0])
#print(upper_series-lower_series)
#plt.title("Final Forecast of commodity price")
#lt.show()
pickle.dump(model, open('model2.pkl','wb'))
model = pickle.load(open('model2.pkl','rb'))
