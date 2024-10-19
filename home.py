import streamlit as st
import pandas as pd
import connectDB as cDB
import psycopg2 as pg
import plotly.express as px

def home():
    print("In HOME")
    with st.container():
        st.write("My Dashboard")
    
    with st.container():
        c0, c1, c2, c3 = st.columns([10,40,40,10])

        with c1:
            with st.container(border=True, height=500):
                st.write("Top Streamed Artists : ")
                sql_query = "SELECT DISTINCT artist FROM"

