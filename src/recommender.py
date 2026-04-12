from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """Represents a song and its attributes."""
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
    """Represents a user's taste preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """Object-oriented recommender that ranks songs based on user preferences."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return top k songs sorted by preference score."""
        def score(song: Song):
            s = 0

            if song.genre == user.favorite_genre:
                s += 2.0

            if song.mood == user.favorite_mood:
                s += 1.5

            s += (1 - abs(song.energy - user.target_energy)) * 2

            if user.likes_acoustic:
                s += song.acousticness
            else:
                s += (1 - song.acousticness)

            return s

        return sorted(self.songs, key=score, reverse=True)[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Generate a human-readable explanation for a recommendation."""
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append("matches your favorite genre")

        if song.mood == user.favorite_mood:
            reasons.append("matches your preferred mood")

        energy_diff = abs(song.energy - user.target_energy)
        if energy_diff < 0.2:
            reasons.append("very close energy level")

        if user.likes_acoustic and song.acousticness > 0.5:
            reasons.append("fits your acoustic preference")

        return ", ".join(reasons) if reasons else "general match"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dictionaries."""
    print(f"Loading songs from {csv_path}...")
    songs = []

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    print(f"Loaded songs: {len(songs)}")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Compute a score and explanation for a song based on user preferences."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs["mood"]:
        score += 1.5
        reasons.append("mood match (+1.5)")

    diff = abs(song["energy"] - user_prefs["energy"])
    energy_score = 1 - diff
    score += energy_score * 2
    reasons.append(f"energy similarity (+{energy_score*2:.2f})")

    if "likes_acoustic" in user_prefs:
        if user_prefs["likes_acoustic"]:
            acoustic_score = song["acousticness"]
        else:
            acoustic_score = 1 - song["acousticness"]

        score += acoustic_score
        reasons.append(f"acoustic match (+{acoustic_score:.2f})")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs and return top k recommendations with explanations."""
    scored = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored.append((song, score, explanation))

    scored.sort(key=lambda x: x[1], reverse=True)

    return scored[:k]