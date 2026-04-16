from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

import csv

def load_songs(csv_path: str) -> List[Dict]:
    print(f"Loading songs from {csv_path}...")
    songs = []

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "title": row["title"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"])
            })

    return songs


def score_song(user_prefs, song):
    score = 0
    reasons = []

    # GENRE
    if song["genre"] == user_prefs["genre"]:
        score += 40
        reasons.append("genre match")

    # MOOD
    if song["mood"] == user_prefs["mood"]:
        score += 30
        reasons.append("mood match")

    # ENERGY
    energy_diff = abs(song["energy"] - user_prefs["energy"])
    energy_score = max(0, 1 - energy_diff) * 20
    score += energy_score
    reasons.append("energy similarity")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    results = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)

        results.append((song, score, explanation))

    # SORT by score descending
    results.sort(key=lambda x: x[1], reverse=True)

    return results[:k]