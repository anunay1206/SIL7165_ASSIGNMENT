# utils.py
# Helper functions used across the project


def read_file(filepath):
    """
    Reads a text file and returns its content as a string
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def normalize_text(text):
    """
    Convert text to lowercase.
    We do NOT remove symbols because substitution cipher uses them.
    """
    return text.lower()


def is_letter(ch):
    """
    Check if character is an English alphabet letter
    """
    return 'a' <= ch <= 'z'


def get_unique_symbols(text):
    """
    Returns a set of unique non-space symbols in the ciphertext
    """
    symbols = set()

    for ch in text:
        if ch != ' ' and ch != '\n':
            symbols.add(ch)

    return symbols
