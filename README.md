# 🎵 AI Music Recommendation System

An AI-powered music recommendation system that uses a **Genetic Algorithm (GA)** to optimize song recommendations according to a user's musical preferences.

The application is built with **Python, DEAP, Pandas, NumPy, and Streamlit** and uses Spotify song metadata and audio features to generate personalized recommendations.

---

## 📌 Project Overview

Traditional recommendation systems often rely on collaborative filtering or user-item interaction history. This project instead treats music recommendation as an **optimization problem**.

Users specify their preferences for:

* Language
* Tempo
* Energy
* Mood (Valence)
* Danceability
* Acousticness

The system calculates how closely each song matches these preferences and uses a **Genetic Algorithm** to search for high-fitness recommendations.

---

# 🏗️ System Architecture

```text
                     Spotify Dataset
                           │
                           ▼
                  Dataset Preprocessing
                           │
                           ▼
                  Cleaned Song Features
                           │
                           ▼
                    User Preferences
                           │
                           ▼
                    Fitness Function
                           │
                           ▼
                   Genetic Algorithm
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
          Selection     Crossover      Mutation
             │             │             │
             └─────────────┴─────────────┘
                           │
                           ▼
                    Best Individuals
                           │
                           ▼
                  Top Recommendations
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
       Recommendation List       GA Convergence
              │                      Plot
              ▼
       Spotify Links &
        Explanations
```

---

# 🔄 Recommendation Workflow

### 1. Load Dataset

The application loads `spotify_tracks.csv` and selects the required fields.

The dataset contains:

* Song name
* Artist
* Language
* Tempo
* Energy
* Valence
* Danceability
* Acousticness
* Popularity
* Album artwork URL
* Spotify track URL

Missing records are removed before recommendation.

---

### 2. Collect User Preferences

Users define their preferred musical characteristics through the Streamlit sidebar.

```text
Language       → Selected language
Tempo          → 60–200 BPM
Energy         → 0.0–1.0
Valence        → 0.0–1.0
Danceability   → 0.0–1.0
Acousticness   → 0.0–1.0
```

---

### 3. Calculate Fitness

Each song receives a fitness score based on how closely it matches the user's preferences.

The fitness function combines:

* Language similarity
* Energy similarity
* Tempo similarity
* Valence similarity
* Danceability similarity
* Acousticness similarity

The implemented weights are:

| Feature      | Weight |
| ------------ | -----: |
| Language     |    35% |
| Energy       |    15% |
| Tempo        |    10% |
| Valence      |    10% |
| Danceability |    15% |
| Acousticness |    15% |

The total fitness score is therefore:

```text
Fitness =
0.35 × Language Similarity
+ 0.15 × Energy Similarity
+ 0.10 × Tempo Similarity
+ 0.10 × Valence Similarity
+ 0.15 × Danceability Similarity
+ 0.15 × Acousticness Similarity
```

---

# 🧬 Genetic Algorithm

The recommendation engine is implemented using **DEAP**.

### Population

The initial population contains:

```text
100 individuals
```

Each individual represents a song index from the dataset.

### Generations

The algorithm runs for:

```text
30 generations
```

### Selection

Tournament selection is used with:

```text
Tournament size = 3
```

### Crossover

Uniform crossover is used with:

```text
Crossover probability = 0.8
```

### Mutation

Uniform integer mutation is used with:

```text
Mutation probability = 0.2
```

The algorithm evaluates the population after each generation and records the best fitness score to visualize convergence.

---

# 🎯 Recommendation Generation

After the final generation:

1. Individuals are sorted by fitness.
2. Duplicate songs are removed.
3. The highest-ranked unique songs are selected.
4. Up to **10 recommendations** are generated.
5. The Streamlit application displays the top **5 recommendations**.

Each recommendation includes:

* Song title
* Artist
* Language
* Tempo
* Energy indicator
* Album artwork
* Spotify app link
* Spotify web-player link

---

# 🖥️ Streamlit Application

The project provides an interactive web interface built using **Streamlit**.

### User Flow

```text
Open Application
       │
       ▼
Select Preferences
       │
       ▼
Generate Recommendations
       │
       ▼
Run Genetic Algorithm
       │
       ▼
Display Top Songs
       │
       ├── Song Details
       ├── Artwork
       ├── Spotify Links
       ├── Explanations
       └── Fitness Convergence Plot
```

The application also provides a short explanation for the recommended songs based on the selected language, energy, and tempo preferences.

---

# 📈 Fitness Convergence

The application plots the best fitness value across generations.

```text
Fitness
  │
  │                ─────────
  │             ──
  │          ──
  │       ──
  │    ──
  │───
  └────────────────────────── Generation
```

This visualization helps demonstrate how the Genetic Algorithm improves or maintains the best solution across generations.

---

# 📂 Project Structure

```text
ai-music-recommendation-system/
│
├── app.py
├── dataset_generator.py
├── ga_engine.py
├── utils.py
├── spotify_tracks.csv
│
├── .streamlit/
│   └── config.toml
│
├── render.yaml
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

| File                     | Purpose                                              |
| ------------------------ | ---------------------------------------------------- |
| `app.py`                 | Streamlit application and user interface             |
| `dataset_generator.py`   | Loads and preprocesses the Spotify dataset           |
| `ga_engine.py`           | Implements the Genetic Algorithm                     |
| `utils.py`               | Fitness calculations and recommendation explanations |
| `spotify_tracks.csv`     | Song metadata and audio features                     |
| `render.yaml`            | Render deployment configuration                      |
| `requirements.txt`       | Python dependencies                                  |
| `.streamlit/config.toml` | Streamlit theme configuration                        |

---

# 📊 Dataset

The project uses a Spotify music dataset containing Indian multilingual tracks and audio-related features.

The dataset includes songs from languages such as:

* Hindi
* Tamil
* Telugu
* Punjabi

The recommendation process uses the following features:

```text
track_name
artist_name
language
tempo
energy
valence
danceability
acousticness
popularity
artwork_url
track_url
```

---

# ⚙️ Installation

## Prerequisites

* Python 3.9+
* pip
* Internet connection for Spotify artwork and links

## 1. Clone the Repository

```bash
git clone https://github.com/garvitgupta17/ai-music-recommendation-system.git
cd ai-music-recommendation-system
```

## 2. Create a Virtual Environment

### macOS / Linux

```bash
python -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start Streamlit with:

```bash
streamlit run app.py
```

The application will open in your browser.

Select your preferences from the sidebar and click:

```text
Generate Recommendations
```

---

# 🚀 Deployment

The project includes a `render.yaml` configuration for deployment on **Render**.

The configured commands are:

```text
Build:
pip install -r requirements.txt

Start:
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

---

# 🛠️ Technologies Used

* **Python** — Core programming language
* **Streamlit** — Interactive web application
* **Pandas** — Dataset processing
* **NumPy** — Numerical calculations
* **Matplotlib** — Fitness convergence visualization
* **DEAP** — Genetic Algorithm implementation

---

# ⚠️ Limitations

This is a **content-based optimization prototype**, rather than a full production recommendation engine.

Current limitations include:

* Recommendations depend on the available Spotify metadata.
* The system does not learn from a user's historical listening behavior.
* Collaborative filtering is not implemented.
* The Genetic Algorithm operates on individual song candidates rather than learning user embeddings.
* The fitness weights are manually defined.
* The `popularity` feature is loaded but is not currently included in the fitness calculation.
* Explanations shown to users summarize only selected preference matches rather than providing a full explanation of the fitness score.

---

# 🔮 Future Improvements

Potential extensions include:

* Add collaborative filtering
* Incorporate listening history and user feedback
* Learn fitness weights automatically
* Add popularity as an optional optimization factor
* Build hybrid recommendation models
* Add genre and artist preferences
* Introduce diversity constraints to avoid overly similar recommendations
* Improve recommendation explanations
* Store user profiles and preferences
* Evaluate recommendation quality using Precision@K, Recall@K, NDCG, and user feedback
* Integrate real-time Spotify APIs

---

# 👤 Author

**Garvit Gupta**

AI & Data Science Student
Interested in **Machine Learning, Data Science, and Data Engineering**.
