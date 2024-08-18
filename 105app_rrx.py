import pandas as pd

import pickle

import streamlit as st

model = pickle.load(open('model.pkl', 'rb'))

def predict(X): 
    return model.predict(X)
  

def getInputs():
    st.button('Predict')
    y = predict(df1)
    return y[0] 

if __name__ == "__main__":
    st.set_page_config(page_title="CSV File Reader',layout='wide")
    # create a title and a subheader
    st.title('Depression & Mood Prediction App')

    st.header('Single File upload')
    upload_file=st.file_uploader("Upload your CSV File")
    df=pd.read_csv(upload_file)
    df1=st.write(df)


    if st.button("Run Analysis"):
        y = getInputs()
        st.write("Analysis completed!")
    if y is not None:
        if y == 0:
            st.write('Predicted Heart Failure: No')
        else:
            st.write('Predicted Heart Failure: Yes')
