# analyzer.py
# Phase 1: Ciphertext analysis

from collections import Counter
from utils import is_letter


def character_frequency(text):
    """
    Count frequency of each non-space character
    """
    freq = Counter()

    for ch in text:
        if ch != ' ' and ch != '\n':
            freq[ch] += 1

    return freq


def word_list(text):
    """
    Extract words from ciphertext
    """
    words = []

    for word in text.split():
        if len(word) > 0:
            words.append(word)

    return words


def word_length_frequency(words):
    """
    Count frequency of word lengths
    """
    length_freq = Counter()

    for word in words:
        length_freq[len(word)] += 1

    return length_freq
