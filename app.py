import streamlit as st
from sklearn import datasets
st.title("CUSTOMER SEGMENTATION")
input_feature=st.sidebar.selectbox("Select Input Feature",("Annual Salary","Spending Score"))
st.text_input("Enter the value",key="input_feature")

def get_data(dataset)