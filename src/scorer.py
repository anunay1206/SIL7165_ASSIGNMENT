# scorer.py
# Quadgram-based scoring for evaluating decryption quality

import math
import os

class QuadgramScorer:
    """
    Scores text based on English quadgram (4-letter sequence) frequencies
    Higher scores indicate more English-like text
    """
    
    def __init__(self, filename="src/quadgrams.txt"):
        """
        Load quadgram frequency database
        
        Args:
            filename: Path to quadgrams file
        """
        self.quadgrams = {}
        self.N = 0
        
        if not os.path.exists(filename):
            raise FileNotFoundError(f"{filename} not found")
        
        print("Loading quadgrams...")
        
        # Load quadgrams and their frequencies
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 2:
                    quad = parts[0].upper()
                    count = int(parts[1])
                    self.quadgrams[quad] = count
                    self.N += count
        
        # Convert counts to log probabilities
        for quad in self.quadgrams:
            self.quadgrams[quad] = math.log10(float(self.quadgrams[quad]) / self.N)
        
        # Floor value for unseen quadgrams
        self.floor = math.log10(0.01 / self.N)
        
        print(f"✓ Loaded {len(self.quadgrams)} quadgrams")
    
    def score(self, text):
        """
        Score text based on quadgram frequencies
        
        Args:
            text: Text to score
            
        Returns:
            Float score (higher = more English-like)
        """
        # Extract only letters and convert to uppercase
        text = ''.join(c.upper() for c in text if c.isalpha())
        
        score = 0
        # Score each consecutive 4-letter sequence
        for i in range(len(text) - 3):
            quad = text[i:i+4]
            score += self.quadgrams.get(quad, self.floor)
        
        return score


# Global scorer instance (initialized once)
SCORER = None

def english_score(text):
    """
    Score text for English-likeness using quadgrams
    
    Args:
        text: Text to score
        
    Returns:
        Float score (higher = more English-like)
    """
    global SCORER
    if SCORER is None:
        SCORER = QuadgramScorer()
    return SCORER.score(text)