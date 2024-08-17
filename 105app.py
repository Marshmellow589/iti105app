import pandas as pd

import pickle

# create a streamlit app

import streamlit as st

st.set_page_config(page_title="CSV File Reader',layout='wide")
# create a title and a subheader
st.title('Depression & Mood Prediction App')

st.header('Single File upload')
upload_file=st.file_uploader("Upload your CSV File")
# df=pd.read_csv(upload_file)
st.dataframe(df,width=1800,height=1200)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)
# load the model
model = pickle.load(open('model.pkl', 'rb'))

def predict(X): 
    y = model.predict(X)
    return y

def getInputs():
     st.button('Predict'):
        y = predict(df)
        return y[0] 

if __name__ == "__main__":
    y = getInputs()
    
    if y is not None:
        if y == 0:
            st.write('Predicted Heart Failure: No')
        else:
            st.write('Predicted Heart Failure: Yes')
