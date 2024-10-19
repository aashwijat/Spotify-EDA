import streamlit as st
import pandas as pd
import connectDB as cDB

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


def myLib():
    print("I am in Home")
   # st.write("#### :green[My Dashboard]")
    myAlbums = load_albums()
    myTracks = load_tracks()
    myArtists = load_artists()
    myMarquee = marquee()

    with st.container():
        c1, c2, c3, c4 = st.columns([25,25,25,25])

        with c1:
            st.write("##### :green[Saved Artists]")
            with st.container(border=True, height=100):
                sql_query = "SELECT count(1) artist FROM \"spotifyEDA.app\".myartists"
                metric1 = cDB.db_get_data_for_metric(sql_query)
                st.metric(":green[#] ",metric1)
        
        with c2:
            st.write("##### :green[Liked Tracks]")
            with st.container(border=True, height=100):
                sql_query = "SELECT count(1) track FROM \"spotifyEDA.app\".mytracks"
                metric2 = cDB.db_get_data_for_metric(sql_query)
                st.metric(":green[#]",metric2)
        
        with c3:
            st.write('##### :green[All Artists You Listen To]')
            with st.container(border=True, height=100):
                sql_query= "SELECT count(DISTINCT artist) FROM \"spotifyEDA.app\".mytracks"
                metric3 = cDB.db_get_data_for_metric(sql_query)
                st.metric(":green[#]", metric3)
        
        with c4:
            st.write('##### :green[All Albums You Listen To]')
            with st.container(border=True, height=100):
                sql_query = "SELECT COUNT(DISTINCT album) FROM \"spotifyEDA.app\".mytracks"
                metric4 = cDB.db_get_data_for_metric(sql_query)
                st.metric(":green[#]",metric4)

    with st.container():
        h_c1, h_c2, h_c3 = st.columns([33,33,33])
        
        #st.write("#### :green[DASHBOARD]")

        with h_c1:
            with st.container(height= 150):
                st.write("##### :green[My Top Artist]")
                my_marquee = pd.DataFrame(myMarquee)
                marq = my_marquee.loc[my_marquee['segment']=='Super Listeners']
                #st.write(marq['artist'], width=500)
                st.data_editor(marq['artist'], width=500, hide_index=True)


            with st.container(border=True,height=450):
                st.write("##### :green[My Saved Albums]")
                my_albums = pd.DataFrame(myAlbums)
                album_Artist = my_albums['artist']
                selected_artist = st.selectbox("#### :blue[Select Artist]",album_Artist.unique(), index=1)
                st.write("##### :green[Albums]")
                album = my_albums.loc[my_albums['artist']==selected_artist,'album']
                st.data_editor(album, hide_index = True, width = 500)

        with h_c2:
            #st.write(" ")
            with st.container(height=620):
                st.write("##### :green[My Artists]")
                my_artists = pd.DataFrame(myArtists)
                all_artists = my_artists['artists']
                st.data_editor(all_artists, hide_index=True, height=550,width=550 )
        
        with h_c3:
            with st.container(height=620):
                st.write("##### :green[My Tracks]")
                my_tracks = pd.DataFrame(myTracks)
                tracks = my_tracks['track'].drop_duplicates()
                st.data_editor(tracks, hide_index=True, height=550, width=550)