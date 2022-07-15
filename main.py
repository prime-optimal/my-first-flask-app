import streamlit as st
import pandas
from streamlit_player import st_player

data = {
    'Series_1': [1, 3, 4, 5, 7],
    'Series 2': [10, 30, 40, 100, 250]
}

df = pandas.DataFrame(data)



st.title('This is Streamlit, baby')
st.subheader('Introducing Tools, which is LIT')
st.write('These streamlit apps should be OBS overlays and plugins')

# Embed a youtube video
st_player("https://youtu.be/CmSKVW1v0xM")

# Embed a music from SoundCloud
st_player("https://soundcloud.com/imaginedragons/demons")
