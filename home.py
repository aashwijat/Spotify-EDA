import streamlit as st
import pandas as pd

#load functions
def load_albums():
    albums = pd.read_csv("myAlbums.csv",on_bad_lines="skip",encoding_errors='ignore', lineterminator='\r')
    return(albums)

def load_artists():
    artists = pd.read_csv("myArtists.csv",on_bad_lines="skip",encoding_errors='ignore',lineterminator='\r')
    return(artists)

def load_tracks():
    tracks = pd.read_csv("myTracks.csv",on_bad_lines="skip",encoding_errors='ignore',lineterminator='\r')
    return(tracks)

def marquee():
    marquee = pd.read_csv("Marquee.csv",on_bad_lines="skip",encoding_errors='ignore',lineterminator='\r')
    return(marquee)


def home():
    print("I am in Home")
   # st.write("#### :green[My Dashboard]")
    myAlbums = load_albums()
    myTracks = load_tracks()
    myArtists = load_artists()
    myMarquee = marquee()
    h_c1, h_c2, h_c3 = st.columns([33,33,33])
    
    with h_c1:
        st.write("#### :green[DASHBOARD]")
        with st.container(border=True, height= 150):
            my_marquee = pd.DataFrame(myMarquee)
            st.write("#### :blue[My Top Artist : ]")
            marq = my_marquee.loc[my_marquee['segment']=='Super Listeners']
            st.write(marq['artist'], width=500)
            

        with st.container(border=True,height=250):
            my_albums = pd.DataFrame(myAlbums)
            album_Artist = my_albums['artist']
            selected_artist = st.selectbox("#### :blue[Select Artist]",album_Artist.unique(), index=1)
            st.write(" :blue[Albums]")
            album = my_albums.loc[my_albums['artist']==selected_artist,'album']
            st.table(album)
