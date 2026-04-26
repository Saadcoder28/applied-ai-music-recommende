"""
Evaluation script.

Runs the recommender + AI explanation pipeline across multiple
user profiles and reports how many generated explanations pass
the guardrail validation check.
"""

from recommender import load_songs, recommend_songs
from rag import load_knowledge
from ai_assistant import generate_explanation
from guardrails import validate_explanation


PROFILES = [
    ("High-Energy Pop", {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.9,
        "likes_acoustic": False,
    }),
    ("Chill Lofi", {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.3,
        "likes_acoustic": True,
    }),
    ("Intense Rock", {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.9,
        "likes_acoustic": False,
    }),
]


def main() -> None:
    songs = load_songs("data/songs.csv")
    knowledge = load_knowledge("knowledge/music_knowledge.txt")

    total = 0
    passed = 0

    for name, prefs in PROFILES:
        print(f"\n=== Evaluating: {name} ===")
        recs = recommend_songs(prefs, songs, k=3)

        for song, score, base_explanation in recs:
            reasons = base_explanation.split(", ") if base_explanation else []
            explanation = generate_explanation(prefs, song, score, reasons, knowledge)

            ok = validate_explanation(explanation)
            total += 1
            if ok:
                passed += 1

            status = "PASS" if ok else "FAIL"
            print(f"[{status}] {song['title']} (score {score:.2f})")
            print(f"   {explanation}")

    print(f"\nGuardrail results: {passed}/{total} passed")


if __name__ == "__main__":
    main()
