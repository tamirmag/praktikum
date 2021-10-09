
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
from flask_cors import CORS, cross_origin
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly_reg = PolynomialFeatures(degree=4)
def train(file):
    # Importing the dataset
    dataset = pd.read_csv('<path>/' + file+'.csv')
    X = dataset.iloc[:, 0:1].values
    y = dataset.iloc[:, 1].values

    # Fitting Polynomial Regression to the dataset

    poly_reg = PolynomialFeatures(degree=4)
    X_poly = poly_reg.fit_transform(X)
    pol_reg = LinearRegression()
    pol_reg.fit(X_poly, y)


    return pol_reg
loc = train('da1')
inter = train('da2')

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def hello_world():
    return render_template('index.html')


@app.route('/calc/<int:amount>/<int:num>/<int:val1>/<int:val2>/<int:val3>/<int:val4>/<int:acc>')
@cross_origin()
def calc(amount,num,val1,val2,val3,val4,acc):
    vals = [val1,val2,val3,val4]
    for i in  range(4-num):
        del vals[-1]
    locals = []
    for v in vals:
        locals.append(0)
    international = 0
    for m in range(0,amount,acc):
        l = loc.predict(poly_reg.fit_transform([[m]])) - loc.predict(poly_reg.fit_transform([[m-acc]]))
        i = inter.predict(poly_reg.fit_transform([[m]])) - inter.predict(poly_reg.fit_transform([[m-acc]]))
        if(l>num*i):
            locals[vals.index(min(vals))]+=1
            vals[vals.index(min(vals))]+=1
        else:
            international+=1
    dict = {
        'locals': locals,
        'international': international
        }
    return dict