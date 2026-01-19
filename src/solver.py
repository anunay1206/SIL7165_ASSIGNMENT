# solver.py
# Main solver using hill climbing optimization

from scorer import english_score
from patterns import generate_frequency_key, generate_random_key, mutate_key
from utils import decrypt_with_key


def hill_climb(ciphertext, initial_key, max_iterations=20000):
    """
    Hill climbing optimization to improve decryption key
    
    Tries random swaps and keeps improvements until convergence
    
    Args:
        ciphertext: Encrypted text
        initial_key: Starting substitution key
        max_iterations: Maximum number of iterations
        
    Returns:
        Tuple of (best_key, best_score)
    """
    current_key = initial_key.copy()
    current_plaintext = decrypt_with_key(ciphertext, current_key)
    current_score = english_score(current_plaintext)
    
    best_key = current_key
    best_score = current_score
    
    no_improvement_count = 0
    
    for iteration in range(max_iterations):
        # Try a random swap
        candidate_key = mutate_key(current_key)
        candidate_plaintext = decrypt_with_key(ciphertext, candidate_key)
        candidate_score = english_score(candidate_plaintext)
        
        # Accept if better
        if candidate_score > current_score:
            current_key = candidate_key
            current_score = candidate_score
            no_improvement_count = 0
            
            # Update best if this is the best so far
            if current_score > best_score:
                best_key = current_key
                best_score = current_score
        else:
            no_improvement_count += 1
        
        # Early stopping if stuck
        if no_improvement_count > 1000:
            break
    
    return best_key, best_score


def solve(ciphertext, max_restarts=30):
    """
    Solve substitution cipher using hill climbing with multiple restarts
    
    Strategy:
    - First half of restarts: Use frequency analysis as starting point
    - Second half: Use random keys for diversity
    - Early termination if no improvement for 15 consecutive restarts
    
    Args:
        ciphertext: Encrypted text to decrypt
        max_restarts: Maximum number of restart attempts
        
    Returns:
        Best decryption key found
    """
    print(f"\n{'='*70}")
    print("SUBSTITUTION CIPHER SOLVER")
    print(f"{'='*70}\n")
    
    best_key = None
    best_score = float('-inf')
    no_improvement_count = 0
    
    for restart in range(max_restarts):
        # Choose starting key strategy
        if restart < max_restarts // 2:
            # Use frequency analysis for first half
            initial_key = generate_frequency_key(ciphertext)
        else:
            # Use random keys for second half
            initial_key = generate_random_key(ciphertext)
        
        # Run hill climbing
        key, score = hill_climb(ciphertext, initial_key, max_iterations=20000)
        
        # Check if this is the best solution so far
        if score > best_score:
            best_key = key.copy()
            best_score = score
            plaintext = decrypt_with_key(ciphertext, key)
            
            print(f"✓ Attempt {restart + 1}: Score = {score:.1f} [IMPROVEMENT]")
            print(f"  {plaintext[:75]}...\n")
            
            no_improvement_count = 0
        else:
            no_improvement_count += 1
        
        # Early stopping if no improvement for many attempts
        if no_improvement_count >= 15:
            print(f"No improvement for 15 attempts. Stopping early at attempt {restart + 1}/{max_restarts}")
            break
    
    print(f"\n{'='*70}")
    print(f"DECRYPTION COMPLETE")
    print(f"Final Score: {best_score:.1f}")
    print(f"{'='*70}\n")
    
    return best_key