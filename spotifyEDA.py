import streamlit as st 
import pandas as pd
import home as h
import connectDB as cDB
import myLibrary as myLib

## page configuration
st.set_page_config(layout="wide",page_title = "melody meets metrics")
st.title(":green[Melody Meets Metrics : Spotify Data Analysis]", anchor=None)
st.subheader("Welcome Aashwija!")
st.logo("logo.png")

# # creating tabs
tab1, tab2, tab3 = st.tabs(["Home","My Library","Upload Data"])

with tab1:
    h.home()

with tab2:
    myLib.myLib()

with tab3:
    cDB.main_load_data()
