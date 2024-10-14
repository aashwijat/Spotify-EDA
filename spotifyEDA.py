import streamlit as st 
import pandas as pd


## page configuration
st.set_page_config(layout="wide",page_title = "melody meets metrics")
st.title(":green[Melody Meets Metrics : Spotify Data Analysis]", anchor=None)
st.subheader(f"Welcome Aashu!")
st.logo("logo.png")

# # creating tabs
tab1, tab2, tab3,tab4 = st.tabs(["Home","My Library","Listening History","Analytics"])

def home():
    st.write("#### :green[My Dashboard]")


with tab1:
    home()