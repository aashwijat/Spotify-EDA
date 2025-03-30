import streamlit as st
import pandas as pd
import connectDB as cDB
import psycopg2 as pg
import plotly.express as px
import calplot
import matplotlib.pyplot as plt

def analysis():
    print("In HOME")
    with st.container():
        st.write("### :green[My Analysis]")
    
    with st.container():
        c1, c2, c3, c4 = st.columns([25,25,25,25])

        with c1:
            st.write("##### Saved Artists")
            with st.container(border=True, height=100):
                sql_query = "SELECT count(1) artist FROM \"spotifyEDA.app\".myartists"
                metric1 = cDB.db_get_data_for_metric(sql_query)
                st.metric(":green[#] ",metric1)
        
        with c2:
            st.write("##### Liked Tracks")
            with st.container(border=True, height=100):
                sql_query = "SELECT count(1) track FROM \"spotifyEDA.app\".mytracks"
                metric2 = cDB.db_get_data_for_metric(sql_query)
                st.metric(":green[#]",metric2)
        
        with c3:
            st.write('##### All Artists You Listen To')
            with st.container(border=True, height=100):
                sql_query= "SELECT count(DISTINCT artist) FROM \"spotifyEDA.app\".mytracks"
                metric3 = cDB.db_get_data_for_metric(sql_query)
                st.metric(":green[#]", metric3)
        
        with c4:
            st.write('##### All Albums You Listen To')
            with st.container(border=True, height=100):
                sql_query = "SELECT COUNT(DISTINCT album) FROM \"spotifyEDA.app\".mytracks"
                metric4 = cDB.db_get_data_for_metric(sql_query)
                st.metric(":green[#]",metric4)

    
    with st.container():
        c1,c2,c3=st.columns([50,2,48])
        with c1:
            with st.container(height= 105):
                sql_query= "SELECT artist, segment FROM \"spotifyEDA.app\".marquee "\
                            "WHERE segment=\'Super Listeners\' "
                metric5 = cDB.db_get_data_for_metric(sql_query)
                st.metric(":green[Top Artist]",metric5['artist'])

            with st.container(border=True, height=450):
                st.write("##### :green[Top Streamed Artists]")
                sql_query = "SELECT \"artistName\", SUM(\"minPlayed\") FROM \"spotifyEDA.app\".streaming_history "\
                            "GROUP BY \"artistName\" ORDER BY SUM(\"minPlayed\") DESC "\
                            "LIMIT 5"
                get_data = cDB.db_get_data_for_chart(sql_query)
                #st.data_editor(get_data['trackName'],height=525, use_container_width=True, hide_index=True)
                st.bar_chart(get_data,x='artistName',y='sum',
                             y_label="Minutes Played",
                             x_label="Artist",
                             horizontal=False,
                             height = 360,
                             color = '#70ccbb'
                             ) 
            
            
            

        with c3:
            with st.container(border=True):
                sql_query="SELECT \"trackName\",SUM(\"minPlayed\") FROM "\
                        "\"spotifyEDA.app\".streaming_history "\
                        "GROUP BY \"trackName\" ORDER BY SUM(\"minPlayed\") DESC "\
                        "LIMIT 5"
                get_data = cDB.db_get_data_for_metric(sql_query)
                st.metric('##### :green[Top Streamed Song]',get_data['trackName'])
            with st.container(border=True, height=450):
                st.write("#### :green[Artist Streaming]")
                sql_query = "SELECT segment as category, COUNT(segment) frq FROM \"spotifyEDA.app\".marquee "\
                            "GROUP BY segment "\
                            "ORDER BY COUNT(segment) "
                chart_data = cDB.db_get_data_for_chart(sql_query)
                fig = px.pie(chart_data, values='frq', names='category',
                             color_discrete_sequence=('#70ccbb','#2f6e62'))
                st.plotly_chart(fig,theme=None)
       
        with st.container(border=True, height=450):
            st.write("#### :green[My Listening Activity]")
            sql_query = "SELECT \"endTime\" FROM \"spotifyEDA.app\".streaming_history"
            df = cDB.db_get_data_for_chart(sql_query)
            df['endTime'] = pd.to_datetime(df['endTime'],format="%d-%m-%Y %H:%M", errors='coerce')
            df['date'] = df['endTime'].dt.date  
            daily_counts = df['date'].value_counts().sort_index()
            daily_counts.index = pd.to_datetime(daily_counts.index)
            daily_counts.index = pd.to_datetime(daily_counts.index, format='%Y-%m')
            fig, ax = calplot.calplot(daily_counts, cmap='viridis', edgecolor='black', dayticks=True)
            st.pyplot(fig)
        with st.expander("##### My Top Tracks"):
            sql_query="SELECT \"trackName\",SUM(\"minPlayed\") FROM "\
                        "\"spotifyEDA.app\".streaming_history "\
                        "GROUP BY \"trackName\" ORDER BY SUM(\"minPlayed\") DESC "\
                        "LIMIT 20"
            get_data = cDB.db_get_data_for_chart(sql_query)
            st.data_editor(get_data['trackName'],width=1500, hide_index=True)

    
