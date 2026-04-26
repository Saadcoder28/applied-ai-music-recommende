"""
Guardrails for validating AI-generated explanations.

Ensures explanations reference real song features such as
genre, mood, or energy. Prevents misleading or generic output.
"""

REQUIRED_TERMS = ("genre", "mood", "energy")


def validate_explanation(explanation: str) -> bool:
    """Return True if the explanation mentions genre, mood, or energy."""
    if not explanation:
        return False
    text = explanation.lower()
    return any(term in text for term in REQUIRED_TERMS)


def guardrail_warning() -> str:
    """Return the warning message appended when validation fails."""
    return "[WARNING] Explanation may be too generic — does not reference genre, mood, or energy."
