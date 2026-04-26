"""
Command line runner for the Music Recommender Simulation.

Now extended with a RAG-based AI explanation system and
guardrail validation on top of the existing recommender.
"""

from recommender import load_songs, recommend_songs
from rag import load_knowledge
from ai_assistant import generate_explanation


def main() -> None:
    songs = load_songs("data/songs.csv")
    knowledge = load_knowledge("knowledge/music_knowledge.txt")

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

    # LOOP through profiles
    for name, user_prefs in profiles:
        print(f"\n=== {name} Profile ===\n")

        recommendations = recommend_songs(user_prefs, songs, k=5)

        for song, score, base_explanation in recommendations:
            reasons = base_explanation.split(", ") if base_explanation else []
            ai_explanation = generate_explanation(
                user_prefs, song, score, reasons, knowledge
            )

            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Explanation: {ai_explanation}")
            print()


if __name__ == "__main__":
    main()
