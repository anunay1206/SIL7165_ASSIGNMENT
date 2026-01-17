# solver.py
# Substitution cipher solver

import random
from scorer import english_score
from collections import Counter

ENGLISH_FREQ_ORDER = "etaoinrshdlucmfwypvbgkjqxz"

def decrypt_with_key(text, key):
    """
    Decrypt ciphertext using substitution key.
    key: dict mapping cipher_char -> plaintext_char
    """
    result = []

    for ch in text:
        if ch in key:
            result.append(key[ch])
        else:
            result.append(ch)

    return "".join(result)
    

def initial_key_from_frequency(text):
    """
    Generate initial substitution key using frequency analysis
    """
    freq = Counter()

    for ch in text:
        if ch != ' ' and ch != '\n':
            freq[ch] += 1

    # sort cipher symbols by frequency
    cipher_symbols = [item[0] for item in freq.most_common()]

    key = {}

    for i in range(min(len(cipher_symbols), 26)):
        key[cipher_symbols[i]] = ENGLISH_FREQ_ORDER[i]

    return key


def mutate_key(key):
    """
    Create a new key by swapping two plaintext letter assignments
    """
    new_key = key.copy()

    if len(new_key) < 2:
        return new_key

    k1, k2 = random.sample(list(new_key.keys()), 2)

    new_key[k1], new_key[k2] = new_key[k2], new_key[k1]

    return new_key

def hill_climb(ciphertext, max_iterations=15000):
    """
    Improve key using hill climbing
    """
    # initial key
    current_key = initial_key_from_frequency(ciphertext)
    current_plain = decrypt_with_key(ciphertext, current_key)
    current_score = english_score(current_plain)

    best_key = current_key
    best_score = current_score

    for _ in range(max_iterations):
        candidate_key = mutate_key(current_key)
        candidate_plain = decrypt_with_key(ciphertext, candidate_key)
        candidate_score = english_score(candidate_plain)

        if candidate_score > current_score:
            current_key = candidate_key
            current_score = candidate_score

            if candidate_score > best_score:
                best_key = candidate_key
                best_score = candidate_score

    return best_key, best_score


def solve(ciphertext, restarts=50):
    """
    Full solver with random restarts
    """
    best_key = None
    best_score = float("-inf")

    for _ in range(restarts):
        key, score = hill_climb(ciphertext)

        if score > best_score:
            best_key = key
            best_score = score

    return best_key
