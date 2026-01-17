# patterns.py
# Word pattern extraction


def word_pattern(word):
    """
    Convert a word into its pattern form.
    Example:
    'xqqx' -> A B B A
    """
    mapping = {}
    pattern = []
    next_char = 'A'

    for ch in word:
        if ch not in mapping:
            mapping[ch] = next_char
            next_char = chr(ord(next_char) + 1)

        pattern.append(mapping[ch])

    return ''.join(pattern)


def build_word_patterns(words):
    """
    Build dictionary:
    word -> pattern
    """
    patterns = {}

    for word in words:
        patterns[word] = word_pattern(word)

    return patterns


def pattern_frequency(patterns):
    """
    Count how often each pattern occurs
    """
    freq = {}

    for pat in patterns.values():
        freq[pat] = freq.get(pat, 0) + 1

    return freq
