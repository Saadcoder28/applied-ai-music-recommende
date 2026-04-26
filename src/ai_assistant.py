"""
AI explanation generator.

Combines the recommender's score and reasons with retrieved
knowledge from the RAG module, then validates the result with
the guardrail. If validation fails, a warning is appended.
"""

from typing import Dict, List

from rag import retrieve
from guardrails import validate_explanation, guardrail_warning


def build_query(user_prefs: Dict, song: Dict) -> str:
    """Build a retrieval query from user preferences and song features."""
    parts = [
        song.get("genre", ""),
        song.get("mood", ""),
        user_prefs.get("genre", ""),
        user_prefs.get("mood", ""),
    ]
    energy = song.get("energy", 0.0)
    parts.append("high energy" if energy >= 0.6 else "low energy chill")
    if song.get("acousticness", 0.0) > 0.5:
        parts.append("acoustic")
    return " ".join(p for p in parts if p)


def generate_explanation(
    user_prefs: Dict,
    song: Dict,
    score: float,
    reasons: List[str],
    knowledge_chunks: List[str],
) -> str:
    """Generate an enhanced explanation and append a guardrail warning if needed."""
    base = ", ".join(reasons) if reasons else "general match"

    query = build_query(user_prefs, song)
    retrieved = retrieve(query, knowledge_chunks, top_k=2)
    context = " ".join(retrieved)

    if context:
        explanation = f"This song matches your preferences ({base}). Context: {context}"
    else:
        explanation = f"This song matches your preferences ({base})."

    if not validate_explanation(explanation):
        explanation = f"{explanation} {guardrail_warning()}"

    return explanation
