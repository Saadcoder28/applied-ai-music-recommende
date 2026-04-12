"""
Command line runner for the Music Recommender Simulation.
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Multiple profiles for evaluation
    profiles = [
        ("High-Energy Pop", {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9,
            "likes_acoustic": False
        }),
        ("Chill Lofi", {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.3,
            "likes_acoustic": True
        }),
        ("Intense Rock", {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.9,
            "likes_acoustic": False
        }),
        ("Edge Case (Conflicting)", {
            "genre": "pop",
            "mood": "sad",
            "energy": 0.9,
            "likes_acoustic": True
        })
    ]

    # LOOP through profiles ✅
    for name, user_prefs in profiles:
        print(f"\n=== {name} Profile ===\n")

        recommendations = recommend_songs(user_prefs, songs, k=5)

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()