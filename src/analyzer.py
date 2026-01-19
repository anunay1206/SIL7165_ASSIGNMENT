# analyzer.py
# Frequency analysis for ciphertext

from collections import Counter
from utils import is_cipher_char


def get_frequency_order(text):
    """
    Get cipher characters sorted by frequency (descending)
    
    This is used to generate initial keys via frequency analysis
    
    Args:
        text: Ciphertext string
        
    Returns:
        List of cipher characters sorted by frequency
    """
    freq = Counter()
    for ch in text:
        if is_cipher_char(ch):
            freq[ch] += 1
    
    sorted_chars = [item[0] for item in freq.most_common()]
    return sorted_chars