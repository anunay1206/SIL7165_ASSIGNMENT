# scorer.py
# English language scoring functions


COMMON_BIGRAMS = [
    "th", "he", "in", "er", "an", "re", "on", "at", "en", "nd"
]

COMMON_TRIGRAMS = [
    "the", "and", "ing", "ent", "ion", "for", "tha"
]

RARE_PATTERNS = [
    "zx", "qj", "jq", "xz", "qq"
]


def english_score(text):
    """
    Returns a numeric score representing how English-like the text is
    Higher score = more likely English
    """
    score = 0
    text = text.lower()

    # bigram scoring
    for bg in COMMON_BIGRAMS:
        score += text.count(bg) * 5

    # trigram scoring
    for tg in COMMON_TRIGRAMS:
        score += text.count(tg) * 10

    # penalty for unlikely sequences
    for rp in RARE_PATTERNS:
        score -= text.count(rp) * 20

    return score
