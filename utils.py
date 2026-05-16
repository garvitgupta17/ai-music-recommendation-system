import numpy as np

def gaussian_similarity(x, y, sigma=20):
    return np.exp(-(x - y)**2 / (2 * sigma**2))

def jaccard_similarity(a, b):

    a = {a}
    b = {b}

    intersection = len(a & b)
    union = len(a | b)

    return intersection / union


def compute_fitness(song, user_pref):
    """
    Calculates similarity score between song features
    and user preferences using weighted similarity metrics.
    """

    score = 0

    score += 0.35 * jaccard_similarity(
        song["language"],
        user_pref["language"]
    )

    score += 0.15 * gaussian_similarity(
        song["energy"],
        user_pref["energy"]
    )

    score += 0.10 * gaussian_similarity(
        song["tempo"],
        user_pref["tempo"]
    )

    score += 0.10 * gaussian_similarity(
        song["valence"],
        user_pref["valence"]
    )

    score += 0.15 * gaussian_similarity(
        song["danceability"],
        user_pref["danceability"]
    )

    score += 0.15 * gaussian_similarity(
        song["acousticness"],
        user_pref["acousticness"]
    )

    return score



def generate_explanation(song, pref):

    return f"""
    This song was recommended because it closely matches
    your preferred language ({pref['language']}), energy level
    ({song['energy']:.2f}), and tempo
    ({song['tempo']:.1f} BPM).
    """