# patterns.py
# Key generation and mutation for hill climbing

import random
from utils import is_cipher_char
from analyzer import get_frequency_order

# English letter frequency order (most to least common)
ENGLISH_FREQ_ORDER = "etaoinshrdlcumwfgypbvkjxqz"


def generate_frequency_key(text):
    """
    Generate initial substitution key using frequency analysis
    
    Maps most frequent cipher symbols to most frequent English letters
    
    Args:
        text: Ciphertext string
        
    Returns:
        Dictionary mapping cipher chars to plaintext chars
    """
    cipher_symbols = get_frequency_order(text)
    key = {}
    
    for i, cipher_char in enumerate(cipher_symbols):
        if i < 26:
            key[cipher_char] = ENGLISH_FREQ_ORDER[i]
    
    return key


def generate_random_key(text):
    """
    Generate a random substitution key
    
    Args:
        text: Ciphertext string
        
    Returns:
        Dictionary mapping cipher chars to plaintext chars
    """
    symbols = [ch for ch in set(text) if is_cipher_char(ch)]
    letters = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(letters)
    
    return dict(zip(symbols, letters[:len(symbols)]))


def mutate_key(key):
    """
    Create a new key by swapping two random letter mappings
    
    This is the core mutation operation for hill climbing
    
    Args:
        key: Current substitution key
        
    Returns:
        New key with one random swap
    """
    new_key = key.copy()
    
    if len(new_key) < 2:
        return new_key
    
    # Pick two random cipher characters and swap their plaintext mappings
    a, b = random.sample(list(new_key.keys()), 2)
    new_key[a], new_key[b] = new_key[b], new_key[a]
    
    return new_key