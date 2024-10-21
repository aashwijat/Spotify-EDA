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
            with st.container(border=True, height=550):
                st.write("Top Streamed Artists : ")
                sql_query = "SELECT \"artistName\", SUM(\"minPlayed\") FROM \"spotifyEDA.app\".streaming_history "\
                            "GROUP BY \"artistName\" ORDER BY SUM(\"minPlayed\") DESC "\
                            "LIMIT 5"
                get_data = cDB.db_get_data_for_chart(sql_query)
                st.data_editor(get_data['artistName'],height=525, use_container_width=True, hide_index=True)

