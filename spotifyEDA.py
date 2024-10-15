import streamlit as st 
import pandas as pd

#load functions
def load_albums():
    albums = pd.read_csv("myAlbums.csv",on_bad_lines="skip",encoding='utf-8',encoding_errors='ignore', lineterminator='\r')
    return(albums)

def load_artists():
    artists = pd.read_csv("myArtists.csv",on_bad_lines="skip",encoding='utf-8',encoding_errors='ignore',lineterminator='\r')
    return(artists)

def load_tracks():
    tracks = pd.read_csv("myTracks.csv",on_bad_lines="skip",encoding='utf-8',encoding_errors='ignore',lineterminator='\r')
    return(tracks)

def marquee():
    marquee = pd.read_csv("Marquee.csv",on_bad_lines="skip",encoding='utf-8',encoding_errors='ignore',lineterminator='\r')
    return(marquee)

## page configuration
st.set_page_config(layout="wide",page_title = "melody meets metrics")
st.title(":green[Melody Meets Metrics : Spotify Data Analysis]", anchor=None)
st.subheader(f"Welcome Aashu!")
st.logo("logo.png")

# # creating tabs
tab1, tab2, tab3,tab4 = st.tabs(["Home","My Library","Listening History","Analytics"])

def home():
    print("I am in Home")
    st.write("#### :green[My Dashboard]")
    myAlbums = load_albums()
    myTracks = load_tracks()
    myArtists = load_artists()
    h_c1, h_c2, h_c3 = st.columns([33,33,33])
    
    with h_c1:
        st.write(":green[My Albums]")
        with st.container(border=True,height=650):
            select_album = st.selectbox("Album : ",myAlbums, index=None)



with tab1:
    home()


