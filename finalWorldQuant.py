#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 23:53:31 2018

@author: vothiquynhyen
"""

# =============================================================================
# I followed the instructions for the project to choose the appropriate stock, in this case AMZN. I downloaded m
# monthly data for Amazon, and the result is a single figure for each month that represents the price of
# the stock for the whole month.
# =============================================================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
    
def linearregression():
    x = np.asarray(list).reshape(-1,1)
    y = np.asarray(out).reshape(-1,1)
    from sklearn.linear_model import LinearRegression
    model = LinearRegression(fit_intercept=True)

    model.fit(x, y)

#    xfit = np.linspace(0, 10, 1000)
#    yfit = model.predict(xfit[:, np.newaxis])

    plt.scatter(x, y)
#    plt.plot(xfit, yfit);
    plt.show()
    
    
def exponentialsmoothing(data,alpha=0.25):
    global out
    out = []
    out.append(data[0])
    for i in range(len(data)):
        if i>0:
            value=alpha*data[i] + (1-alpha)*out[i-1]
            out.append(value)
    return out


def main():
    

    data1 = pd.read_csv("/Users/vothiquynhyen/Documents/AMZNdata.csv")
    data1.describe()
    type(data1)
    data1 = data1.iloc[0:,1:]
    data1
    plt.plot(data1)
    arr = data1.values
    arr
    type(arr)
    global list
    list = arr[0].tolist()
    list
    list[1]    
    arr
    plt.ion()
    plt.plot(list)
    plt.show()
    ok = "no"
    while ok != "yes":
        
        alpha = input("enter your alpha for calculation:")
        exponentialsmoothing(list,alpha)
        plt.ion()
        plt.clf()
        plt.plot(  out, color='red', linewidth=4)
        plt.plot( list, color='olive', linewidth=2)
        plt.show()
        ok = raw_input("are you happy with the result?(yes/no)")
    ninth=alpha*list[7] + (1-alpha)*out[7]
    
    print "prediction for next month is ",ninth
    linearregression()
    print "ggggg"

    
       
    
if __name__ == "__main__": main()


    
    