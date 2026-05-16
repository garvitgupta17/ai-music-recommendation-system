import streamlit as st
import pandas as pd


@st.cache_data
def load_dataset():

    df = pd.read_csv("spotify_tracks.csv")

    needed_columns = [
        "track_name",
        "artist_name",
        "language",
        "tempo",
        "energy",
        "valence",
        "danceability",
        "acousticness",
        "popularity",
        "artwork_url",
        "track_url"
    ]

    df = df[needed_columns]

    df.columns = [
        "song_title",
        "artist",
        "language",
        "tempo",
        "energy",
        "valence",
        "danceability",
        "acousticness",
        "popularity",
        "artwork_url",
        "track_url"
    ]

    df.dropna(inplace=True)

    return df