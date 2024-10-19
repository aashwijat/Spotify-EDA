import streamlit as st 
import pandas as pd
import home as h
import connectDB as cDB

## page configuration
st.set_page_config(layout="wide",page_title = "melody meets metrics")
st.title(":green[Melody Meets Metrics : Spotify Data Analysis]", anchor=None)
st.subheader(f"Welcome Aashu!")
st.logo("logo.png")

# # creating tabs
tab1, tab2 = st.tabs(["Home","Upload Data"])

with tab1:
    h.home()

with tab2:
    cDB.main_load_data()
