import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 


#from PIL import Image

#pickle_in = open("model.pkl","rb")
#model=pickle.load(pickle_in)





import tensorflow as tf

# Load the model
model = tf.keras.models.load_model("C:/Users\PRIYAM SAHA\Desktop\PROJECTS\SunbaseData Assignment\model.h5")











#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict(Age, Gender, Location, Subscription_Length_Months, Monthly_Bill, Total_Usage_GB):
    
    if Gender == 'Male':
        Gender = 1
    else:
        Gender = 0
    
    if Location == 'Los Angeles':
        Location = 2
    elif Location == 'New York':
        Location = 4
    elif Location == 'Miami':
        Location = 3
    elif Location == 'Chicago':
        Location = 0
    elif Location == 'Houston':
        Location = 1
    
    
    
    #Age = 24
    #Gender = 1
    #Location = 2
    #Subscription_Length_Months = 21
    #Monthly_Bill = 1000
    #Total_Usage_GB = 1200
    
    Age = float(Age)
    Subscription_Length_Months = float(Subscription_Length_Months)
    Monthly_Bill = float(Monthly_Bill)
    Total_Usage_GB = float(Total_Usage_GB)
    
    
    prediction=model.predict([[Age, Gender, Location, Subscription_Length_Months, Monthly_Bill, Total_Usage_GB]])
    print(prediction[0][0])
    if prediction[0][0] >= 0.5:
        result = 1
    else:
        result = 0
    print(result)
    return result



def main():
    #st.title("Customer Churn Predictor App")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Customer Churn Predictor App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.text_input("Age")
    Gender = st.text_input("Gender (Male or Female)")
    Location = st.text_input("Location ('Los Angeles', 'New York', 'Miami', 'Chicago', 'Houston')")
    Subscription_Length_Months = st.text_input("Subscription Length (in Months)")
    Monthly_Bill = st.text_input("Monthly Bill")
    Total_Usage_GB = st.text_input("Total Data Usage (in GB)")
    churn=""
    if st.button("Predict Customer Churn"):
        churn=predict(Age, Gender, Location, Subscription_Length_Months, Monthly_Bill, Total_Usage_GB)
    st.success('The output is {}'.format(churn))
    if st.button("Customer Churn Key"):
        st.text("Churned - 1")
        st.text("Retained - 0")

if __name__=='__main__':
    main()
