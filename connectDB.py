import psycopg2 as pg
from sqlalchemy import create_engine
import streamlit as st
import pandas as pd
import os

def save_uploaded_file(user_dir, uploaded_file):
    os.makedirs(user_dir,exist_ok=True)
    file_path= os.path.join(user_dir, uploaded_file.name)
    with open(file_path,"wb") as f:
        f.write(uploaded_file.getbuffer())
        f.close()
    return uploaded_file.name

def upload_click_button():
    st.session_state.upload_clicked=True

if 'upload_clicked' not in st.session_state:
    st.session_state.upload_clicked = False
    
#def connect_2_db():
db_details = { 
    #PostgreSQL
    "user": 'postgres',
    "password":'art#1234',
    "host": 'localhost',
    "port":'5432',
    "database": 'SpotifyEDA',
    "schema_name": 'spotifyEDA.app' }
 

def bulk_insert_from_dataframe(df, db_schema, table_name):
    connect = "postgresql+psycopg2://%s:%s@%s:5432/%s" %(
        db_details['user'],
        db_details['password'],
        db_details['host'],
        db_details['database']
    )
    #print("Table Name : ",table_name)
    #print("Number of Records : ", len(df))
    engine = create_engine(connect)
  #  print("Connected")
    number_of_records = df.to_sql(
        table_name,
        con=engine,
        schema = db_schema,
        index=False,
        if_exists = 'replace'
        
    )
    return number_of_records
def main_load_data():
    ld_col1, ld_col2, ld_col3 = st.columns([25,55,20])
    with ld_col1:
        with st.form("Load Bulk Records",border=False):
            uploaded_data_file = st.file_uploader("Upload File",[".csv",".txt"],accept_multiple_files=False)
            table_selected = st.text_input("Table Name")
            table_selected= table_selected.lower()
            load_data_clicked = st.form_submit_button("Load Data")
            #st.write(st.session_state)
    
    with ld_col2:
        if uploaded_data_file and table_selected and load_data_clicked:
            uploaded_files_path = f".\\"
            csv_file = save_uploaded_file(uploaded_files_path,uploaded_data_file)
            df = pd.read_csv(csv_file)
            df = st.data_editor(df,height=525, use_container_width=True, hide_index=True)
            st.session_state["df"] = df
            if len(st.session_state["df"])>0:
                st.button("Upload Data to Table", on_click = upload_click_button)
    
    with ld_col3:
        if st.session_state.upload_clicked:
            db_schema = "spotifyEDA.app"
            number_of_records = bulk_insert_from_dataframe(pd.DataFrame(st.session_state["df"]), db_schema, table_selected)
            st.success(f"Data File Uploaded")
            st.success(f"Table Name: {table_selected}")
            st.success(f"Number of records : {number_of_records}")

def db_connect(db_details):
    db_conn = pg.connect(
        database = db_details["database"],
        host = db_details["host"],
        user= db_details["user"],
        password = db_details["password"],
        port = db_details["port"]
    )
    return db_conn

def db_get_data_for_metric(sql_query):
    db_conn = db_connect(db_details)
    result_set_df = pd.read_sql_query(sql_query, db_conn)
    db_conn.close()
    return result_set_df.iloc[0]

def db_get_data_for_chart(sql_query):
    db_conn = db_connect(db_details)
    result_set_df = pd.read_sql_query(sql_query, db_conn)
    db_conn.close()
    return result_set_df