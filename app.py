import streamlit as st
import matplotlib.pyplot as plt

from dataset_generator import load_dataset
from ga_engine import run_ga
from utils import generate_explanation

st.set_page_config(
    page_title="AI Music Recommender",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 AI Music Recommendation System")

st.markdown(
    """
    Personalized music recommendations using
    Genetic Algorithms and preference optimization.
    """
)   

dataset = load_dataset()

st.sidebar.success("Customize Your Music Taste")

language = st.sidebar.selectbox(
    "Preferred Language",
    dataset["language"].unique()
)

tempo = st.sidebar.slider("Tempo",60,200,120)

energy = st.sidebar.slider("Energy",0.0,1.0,0.5)

valence = st.sidebar.slider("Mood (Valence)",0.0,1.0,0.5)

danceability = st.sidebar.slider("Danceability",0.0,1.0,0.5)

acousticness = st.sidebar.slider("Acousticness",0.0,1.0,0.5)


if st.button("Generate Recommendations"):

    with st.spinner("Generating AI recommendations..."):

        user_pref = {
            "language": language,
            "tempo": tempo,
            "energy": energy,
            "valence": valence,
            "danceability": danceability,
            "acousticness": acousticness
        }

        recs, history = run_ga(dataset, user_pref)

    st.metric(
        label="Best Fitness Score", 
        value=f"{max(history):.4f}"
    )

    for i, song in enumerate(recs[:5]):

        with st.container():

            col1, col2 = st.columns([1, 4])

            with col1:

                st.image(
                    song["artwork_url"],
                    width=100
                )

            with col2:

                st.markdown(
                    f"### {song['song_title']}"
                )

                st.write(
                    f"Artist: {song['artist']}"
                )

                st.write(
                    f"Language: {song['language']}"
                )

                st.write(
                    f"Tempo: {song['tempo']:.1f} BPM"
                )

                track_id = song["track_url"].split("/")[-1]

                spotify_app_link = f"spotify:track:{track_id}"

                st.markdown(
                    f"""
                    [🎧 Open in Spotify App]({spotify_app_link})  
                    [🌐 Open Web Player]({song['track_url']})
                    """
                )

                st.progress(float(song['energy']))
                st.caption("Energy")

            st.divider()

    st.subheader("Explanation")

    for r in recs[:3]:

        st.write(generate_explanation(r,user_pref))

    st.subheader("GA Convergence Plot")

    fig, ax = plt.subplots()

    ax.plot(
    history,
    linewidth=3
    )

    ax.grid(True)

    ax.set_xlabel("Generation")

    ax.set_ylabel("Fitness")

    ax.set_title("Fitness Convergence")

    st.pyplot(fig)

st.markdown("---")

st.caption(
    "Built using Python, Streamlit, and Genetic Algorithms"
)