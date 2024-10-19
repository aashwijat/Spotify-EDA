# import streamlit as st
# import pandas as pd
# import connectDB as cDB

# #load functions
# def load_albums():
#     albums = pd.read_csv("myAlbums.csv",on_bad_lines="skip",encoding_errors='ignore', lineterminator='\r')
#     return(albums)

# def load_artists():
#     artists = pd.read_csv("myArtists.csv",on_bad_lines="skip",encoding_errors='ignore',lineterminator='\r')
#     return(artists)

# def load_tracks():
#     tracks = pd.read_csv("myTracks.csv",on_bad_lines="skip",encoding_errors='ignore',lineterminator='\r')
#     return(tracks)

# def marquee():
#     marquee = pd.read_csv("Marquee.csv",on_bad_lines="skip",encoding_errors='ignore',lineterminator='\r')
#     return(marquee)


def home():
    print("home")
 
#     print("I am in Home")
#    # st.write("#### :green[My Dashboard]")
#     myAlbums = load_albums()
#     myTracks = load_tracks()
#     myArtists = load_artists()
#     myMarquee = marquee()
#     h_c1, h_c2, h_c3 = st.columns([33,33,33])
    
#     #st.write("#### :green[DASHBOARD]")

#     with h_c1:
#         with st.container(height= 150):
#             st.write("##### :blue[My Top Artist]")
#             my_marquee = pd.DataFrame(myMarquee)
#             marq = my_marquee.loc[my_marquee['segment']=='Super Listeners']
#             #st.write(marq['artist'], width=500)
#             st.data_editor(marq['artist'], width=500, hide_index=True)


#         with st.container(border=True,height=450):
#             st.write("##### :blue[My Saved Albums]")
#             my_albums = pd.DataFrame(myAlbums)
#             album_Artist = my_albums['artist']
#             selected_artist = st.selectbox("#### :green[Select Artist]",album_Artist.unique(), index=1)
#             st.write("##### :blue[Albums]")
#             album = my_albums.loc[my_albums['artist']==selected_artist,'album']
#             st.data_editor(album, hide_index = True, width = 500)

#     with h_c2:
#         st.write(" ")
#         with st.container(height=450):
#             st.write("##### :blue[My Artists]")
#             my_artists = pd.DataFrame(myArtists)
#             all_artists = my_artists['artists/name']
#             st.data_editor(all_artists, hide_index=True, width=500 )