"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")
    # Starter example profile
    profiles = {
    "High Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
    "Chill Lofi": {"genre": "lofi", "mood": "calm", "energy": 0.3},
    "Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95},
    "Weird Edge Case": {"genre": "pop", "mood": "sad", "energy": 0.95}
}

    for name, user_prefs in profiles.items():
        print(f"\n=== {name} ===\n")

        recommendations = recommend_songs(user_prefs, songs, k=5)

        for i, rec in enumerate(recommendations, 1):
            song, score, explanation = rec

            print(f"{i}. {song['title']} ({song['genre']}, {song['mood']})")
            print(f"   Score: {score:.2f}")
            print(f"   Why: {explanation}")
            print()


if __name__ == "__main__":
    main()
