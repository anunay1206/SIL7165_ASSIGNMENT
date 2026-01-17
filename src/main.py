from utils import read_file, normalize_text
from analyzer import word_list
from patterns import build_word_patterns, pattern_frequency

text = read_file("ciphertexts/ciphertext-1.txt")
text = normalize_text(text)

words = word_list(text)
patterns = build_word_patterns(words)
freq = pattern_frequency(patterns)

print("Sample words and patterns:")
for w in list(patterns.keys())[:10]:
    print(w, "->", patterns[w])

print("\nPattern frequency:")
print(freq)
