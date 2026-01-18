# scorer.py - Quadgram scorer for your file
import math
import os

class QuadgramScorer:
    def __init__(self, filename="src/quadgrams.txt"):
        self.quadgrams = {}
        self.N = 0
        
        if not os.path.exists(filename):
            raise FileNotFoundError(f"{filename} not found")
        
        print("Loading quadgrams...")
        
        # Load quadgrams
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 2:
                    quad = parts[0].upper()
                    count = int(parts[1])
                    self.quadgrams[quad] = count
                    self.N += count
        
        # Convert to log probabilities
        for quad in self.quadgrams:
            self.quadgrams[quad] = math.log10(float(self.quadgrams[quad]) / self.N)
        
        # Floor value for unseen quadgrams
        self.floor = math.log10(0.01 / self.N)
        
        print(f"✓ Loaded {len(self.quadgrams)} quadgrams")
    
    def score(self, text):
        """Score text based on quadgram frequencies"""
        # Remove non-letters and convert to uppercase
        text = ''.join(c.upper() for c in text if c.isalpha())
        
        score = 0
        for i in range(len(text) - 3):
            quad = text[i:i+4]
            score += self.quadgrams.get(quad, self.floor)
        
        return score

# Global scorer - initialized once
SCORER = None

def english_score(text):
    global SCORER
    if SCORER is None:
        SCORER = QuadgramScorer()
    return SCORER.score(text)