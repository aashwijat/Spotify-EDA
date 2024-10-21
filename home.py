import streamlit as st
import pandas as pd
import connectDB as cDB
import psycopg2 as pg
import plotly.express as px

def home():
    print("In HOME")
    with st.container():
        st.write("### :green[My Dashboard]")
    
    with st.container():
        c1,c2,c3=st.columns([60,5,35])
        with c1:
            with st.container(border=True):
                st.write("##### Top Streamed Artists")
                sql_query = "SELECT \"artistName\", SUM(\"minPlayed\") FROM \"spotifyEDA.app\".streaming_history "\
                            "GROUP BY \"artistName\" ORDER BY SUM(\"minPlayed\") DESC "\
                            "LIMIT 5"
                get_data = cDB.db_get_data_for_chart(sql_query)
                #st.data_editor(get_data['artistName'],height=525, use_container_width=True, hide_index=True)
                st.bar_chart(get_data,x='artistName',y='sum',
                             y_label="Minutes Played",
                             x_label="Artist",
                             horizontal=False,
                             height = 500,
                             color = '#FFC2B5'
                             )
        with c3:
            with st.container(border=True):
                sql_query="SELECT \"trackName\",SUM(\"minPlayed\") FROM "\
                          "\"spotifyEDA.app\".streaming_history "\
                          "GROUP BY \"trackName\" ORDER BY SUM(\"minPlayed\") DESC "\
                          "LIMIT 5"
                get_data = cDB.db_get_data_for_metric(sql_query)
                st.metric('##### :green[Top Streamed Song]',get_data['trackName'])

                # fig = px.pie(get_data,values='count',names='trackName',title='Top Streamed Songs',
                #              color_discrete_sequence=('#FFB5B5','#ACFF00'))
                # st.plotly_chart(fig,theme=None)
                
                # st.bar_chart(get_data,x='trackName',y='count',
                #              x_label='Streaming Count',
                #              y_label='Track Name',
                #              horizontal=False,
                #              color="#FFF7B5")
            #     fig = px.pie(chart_data, values='disc_count', names='id',title='Discontinued Medicines',
            #                 color_discrete_sequence=('#FF0000','#0000FF'))
            # st.plotly_chart(fig,theme=None)
            with st.expander("##### My Top Tracks"):
                #st.write("##### TOP 20")
                sql_query="SELECT \"trackName\",SUM(\"minPlayed\") FROM "\
                          "\"spotifyEDA.app\".streaming_history "\
                          "GROUP BY \"trackName\" ORDER BY SUM(\"minPlayed\") DESC "\
                          "LIMIT 20"
                get_data = cDB.db_get_data_for_chart(sql_query)
                st.data_editor(get_data['trackName'],width=400,hide_index=True)
