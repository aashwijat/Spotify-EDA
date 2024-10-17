import streamlit as st 
import pandas as pd
import home as h

## page configuration
st.set_page_config(layout="wide",page_title = "melody meets metrics")
st.title(":green[Melody Meets Metrics : Spotify Data Analysis]", anchor=None)
st.subheader(f"Welcome Aashu!")
st.logo("logo.png")

# # creating tabs
tab1, tab2, tab3,tab4 = st.tabs(["Home","My Library","Listening History","Analytics"])

with tab1:
    h.home()


