#importing necessary libraries
import urllib
import time
from flask import Flask, request
import pandas as pd


#Initialize flask app
# app = Flask(__name__)

# #
# @app.route("/", methods=['GET'])
def get_names(): 
    results = pd.read_csv('results.csv', sep=',',header=None)
    stats = pd.read_csv('results.csv', sep=',',header=None)
    print(results)
    print(stats)