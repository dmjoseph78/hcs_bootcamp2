#importing necessary libraries
import urllib
import time
#from flask import Flask, request
import numpy as np


#Initialize flask app
# app = Flask(__name__)

# #
# @app.route("/", methods=['GET'])
def get_names(): 
    results = np.read_csv('results.csv', sep=',',header=None)
    stats = np.read_csv('results.csv', sep=',',header=None)
    print(results)
    print(stats)