import pandas as pd
import math
import pickle

# create a streamlit app

import streamlit as st

# create a title and a subheader
st.title('Mood Depression Prediction App')

# insert image at home page
st.image('1undepression.png', width=500)

# load the model
model = pickle.load(open('model.pkl', 'rb'))

def predict(X): 
    y = model.predict(X)
    return y

# generate streamlit inputs for the following variables: marital_status,arthritis_type,full_time_work,out_of_work,vigorous_recreation,moderate_recreation,lifetime_alcohol_consumption
def getInputs():
 
    with st.sidebar:
        # input for age
        # age = st.slider('age', 20, 120, 30)

        # input for lifetime_alcohol_consumption
        lifetime_alcohol_consumption = st.radio("lifetime_alcohol_consumption", ('no', 'yes') )
        if lifetime_alcohol_consumption == 'no': 
            lifetime_alcohol_consumption = 0
        else:
            lifetime_alcohol_consumption = 1
            
        # input for moderate_recreation
        moderate_recreation = st.radio("moderate_recreation", ('no', 'yes') )
        if moderate_recreation == 'no': 
            moderate_recreation = 0
        else:
            moderate_recreation = 1  
               
        # input for vigorous_recreation
        vigorous_recreation = st.radio("vigorous_recreation", ('no', 'yes') )
        if vigorous_recreation == 'no': 
            vigorous_recreation = 0
        else:
            vigorous_recreation = 1 
            
        # input for full_time_work
        full_time_work = st.radio("full_time_work", ('no', 'yes') )
        if full_time_work == 'no': 
            full_time_work = 0
        else:
            full_time_work = 1 
            
        # input for out_of_work
        out_of_work = st.radio("out_of__work", ('Retired', 'Disabled','Home Caretaker','School','Health','Other') )
        if out_of_work == 'Retired': 
            out_of_work = 1
        elif out_of_work =="Disabled":
             out_of_work = 2
        elif out_of_work == 'Home Caretaker':
             out_of_work = 3
        elif out_of_work == 'School':
            out_of_work = 4
        elif out_of_work =='Health':
            out_of_work =5      
        else:
            out_of_work = 0
            
         # input for marital_status
        marital_status = st.radio("marital_status", ('Married', 'Never Married','Widowed','Divorced','Separated','Partner') )
        if marital_status == 'Married': 
            marital_status = 1
        elif marital_status =="Never Married":
             marital_status = 2
        elif marital_status == 'Widowed':
             marital_status = 3
        elif marital_status == 'Divorced':
            marital_status = 4
        elif marital_status =='Separated':
            marital_status =5      
        else:
            marital_status = 0
            


        values = [[marital_status,full_time_work,out_of_work,vigorous_recreation,moderate_recreation,lifetime_alcohol_consumption]]
    
        if st.button('Predict'):
            y = predict(values)
            return y[0] 



if __name__ == "__main__":
    y = getInputs()
    
    if y is not None:
        if y == 0:
            st.write('Predicted Heart Failure: No')
        else:
            st.write('Predicted Heart Failure: Yes')