# utils.py
# Core utility functions

# Characters that are NOT encrypted (anchors)
ANCHORS = set([" ", ",", ".", ";", "!", "\n"])


def read_file(filepath):
    """
    Read a text file and return its content
    
    Args:
        filepath: Path to the file
        
    Returns:
        File content as string
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def normalize_text(text):
    """
    Convert text to lowercase
    
    Note: We do NOT remove symbols because substitution cipher uses them
    
    Args:
        text: Input text
        
    Returns:
        Lowercase text
    """
    return text.lower()


def is_cipher_char(ch):
    """
    Check if character should be decrypted
    
    Everything except spaces and punctuation is encrypted
    
    Args:
        ch: Character to check
        
    Returns:
        True if character is encrypted, False otherwise
    """
    return ch not in ANCHORS


def decrypt_with_key(text, key):
    """
    Decrypt ciphertext using a substitution key
    
    Args:
        text: Ciphertext string
        key: Dictionary mapping cipher chars to plaintext chars
        
    Returns:
        Decrypted plaintext string
    """
    result = []
    for ch in text:
        if is_cipher_char(ch) and ch in key:
            result.append(key[ch])
        else:
            result.append(ch)
    return "".join(result)