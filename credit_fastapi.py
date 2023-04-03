import uvicorn
from fastapi import FastAPI
import numpy as np
import pandas as pd
import pickle
from dv_credit import credit

# uvicorn credit_fastapi:app --reload

app = FastAPI()
pickle_in = open("credit.pkl","rb")
lr = pickle.load(pickle_in)

# Index route it will directly open this at 
# API 1
@app.get("/")
def index():
    return {'message' : "Hello ! This is our Home page of this API."}

# API 2
@app.get("/{name}")
def get_name(name : str):
    return {'message' : f'Hello {name}'}

# API 3
@app.post('/predict')
def predict_status(data : credit):
    data = data.dict()
    # print(data)
    # print("Hello")
    person_age = data['person_age']
    person_income = data['person_income']	
    person_emp_length = data['person_emp_length']
    loan_amnt = data['loan_amnt']
    loan_int_rate = data['loan_int_rate']
    loan_percent_income = data['loan_percent_income']	
    cb_person_cred_hist_length = data['cb_person_cred_hist_length']
    # print(lr.predict([[age,duration,campaign,pdays,previous,emp_var_rate,cons_price_idx,cons_conf_idx,euribor3m,nr_employed]]))
    # print("hello")
    prediction = lr.predict([[person_age,person_income,person_emp_length,loan_amnt,loan_int_rate,loan_percent_income,cb_person_cred_hist_length]])
    # if prediction[0] == 0:
    #     print("He is defaultee.")
    # else:
    #     print("He is not a defaultee.")




