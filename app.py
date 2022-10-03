# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 22:14:00 2022

@author: Cevher
"""

# Importing Necessary modules
from fastapi import FastAPI,File,UploadFile
import uvicorn
 
# Declaring our FastAPI instance
app = FastAPI()
 
@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}
def hello_name(name : str):
    # Defining a function that takes only string as input and output the
    # following message.
    return {'message': f'Welcome to here!, {name}'}

if __name__=='__main__':
    uvicorn.run(app,host="127.0.0.1",port="8000")