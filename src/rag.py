"""
Simple Retrieval-Augmented Generation (RAG) module.

Loads a local knowledge base and retrieves the most relevant
chunks for a query using basic keyword overlap (no external libraries).
"""

from typing import List


def load_knowledge(path: str = "knowledge/music_knowledge.txt") -> List[str]:
    """Load the knowledge base and split it into non-empty chunks."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = [c.strip() for c in text.split("\n\n") if c.strip()]
    return chunks


def _tokenize(text: str) -> List[str]:
    """Lowercase and split a string into simple word tokens."""
    cleaned = "".join(ch.lower() if ch.isalnum() or ch.isspace() else " " for ch in text)
    return [t for t in cleaned.split() if t]


def retrieve(query: str, chunks: List[str], top_k: int = 2) -> List[str]:
    """Return the top_k chunks most relevant to the query by keyword overlap."""
    query_tokens = set(_tokenize(query))
    if not query_tokens:
        return []

    scored = []
    for chunk in chunks:
        chunk_tokens = set(_tokenize(chunk))
        overlap = len(query_tokens & chunk_tokens)
        if overlap > 0:
            scored.append((overlap, chunk))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [chunk for _, chunk in scored[:top_k]]
