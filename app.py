# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 22:14:00 2022

@author: Cevher
"""

# Importing Necessary modules
from fastapi import FastAPI
import uvicorn
 
# Declaring our FastAPI instance
app = FastAPI()
 
# Defining path operation for root endpoint
@app.get('/')
def main():
    return {'message': 'Get request!'}
 
# Defining path operation for /name endpoint
@app.get('/{name}')
def hello_name(name : str):
    # Defining a function that takes only string as input and output the
    # following message.
    return {'message': f'Welcome to here!, {name}'}