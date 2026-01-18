# solver.py - Simple hill climbing solver
import random
from scorer import english_score
from collections import Counter
from utils import is_cipher_char

def decrypt_with_key(text, key):
    result = []
    for ch in text:
        if is_cipher_char(ch) and ch in key:
            result.append(key[ch])
        else:
            result.append(ch)
    return "".join(result)

def get_freq_key(text):
    """Generate key using frequency analysis"""
    freq = Counter(ch for ch in text if is_cipher_char(ch))
    sorted_cipher = [x[0] for x in freq.most_common()]
    english_order = "etaoinshrdlcumwfgypbvkjxqz"
    
    key = {}
    for i, cipher_char in enumerate(sorted_cipher):
        if i < 26:
            key[cipher_char] = english_order[i]
    return key

def random_key(text):
    """Generate random key"""
    symbols = [ch for ch in set(text) if is_cipher_char(ch)]
    letters = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(letters)
    return dict(zip(symbols, letters[:len(symbols)]))

def swap_random(key):
    """Swap two random letters"""
    new_key = key.copy()
    a, b = random.sample(list(new_key.keys()), 2)
    new_key[a], new_key[b] = new_key[b], new_key[a]
    return new_key

def hill_climb(text, key, max_iter=20000):
    """Hill climbing with random swaps"""
    current = key.copy()
    current_score = english_score(decrypt_with_key(text, current))
    best = current
    best_score = current_score
    
    count = 0
    for i in range(max_iter):
        candidate = swap_random(current)
        candidate_score = english_score(decrypt_with_key(text, candidate))
        
        if candidate_score > current_score:
            current = candidate
            current_score = candidate_score
            count = 0
            
            if current_score > best_score:
                best = current
                best_score = current_score
        else:
            count += 1
            
        # Early stopping if stuck
        if count > 1000:
            break
    
    return best, best_score

def solve(ciphertext, restarts=100):
    """Solve with multiple restarts"""
    print(f"\n{'='*70}")
    print("SUBSTITUTION CIPHER SOLVER")
    print(f"Running {restarts} hill-climbing attempts...")
    print(f"{'='*70}\n")
    
    best_key = None
    best_score = float('-inf')
    
    for i in range(restarts):
        # Use frequency analysis for first half, random for second half
        if i < restarts // 2:
            key = get_freq_key(ciphertext)
        else:
            key = random_key(ciphertext)
        
        # Hill climb
        key, score = hill_climb(ciphertext, key, max_iter=20000)
        
        if score > best_score:
            best_key = key.copy()
            best_score = score
            plaintext = decrypt_with_key(ciphertext, key)
            print(f"✓ Attempt {i+1}/{restarts}: Score = {score:.1f} [NEW BEST]")
            print(f"  {plaintext[:75]}...")
            print()
        elif (i+1) % 20 == 0:
            print(f"  Attempts {i-18}-{i+1}: Best score = {best_score:.1f}")
    
    print(f"\n{'='*70}")
    print(f"FINAL SCORE: {best_score:.1f}")
    print(f"{'='*70}\n")
    
    return best_key