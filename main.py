# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 23:47:34 2021

@author: ameya
"""

#pip install fastapi uvicorn

# 1. Library imports
import uvicorn ##ASGI
from fastapi import FastAPI

# 2. Create the app object
app = FastAPI()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Successful'}

'''4. Route with a single parameter, returns the parameter within a message
    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/Welcome')
def get_name(name: str):
    #return {'Enter the Image url': f'{name}'}'''

# Deployment in Progress
@app.post('/predict')
def predict_age(image_url: str):
    #file_type='image'
    #response = upload_file_to_aws_s3(image_url, file_type)
    #print("image_url:",image_url)
    return image_url


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000/docs
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn main:app --reload