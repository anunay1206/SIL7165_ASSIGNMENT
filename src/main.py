# main.py
# Entry point for substitution cipher solver

import sys
import os
from utils import read_file, normalize_text, decrypt_with_key
from solver import solve


def main():
    """
    Main function to decrypt a ciphertext file
    
    Usage: python3 src/main.py <ciphertext-file>
    """
    if len(sys.argv) != 2:
        print("Usage: python3 src/main.py <ciphertext-file>")
        return

    filename = sys.argv[1]
    path = os.path.join("ciphertexts", filename)

    if not os.path.exists(path):
        print("File not found:", path)
        return

    print("\nDecrypting:", filename)
    print("=" * 60)

    # Read and normalize ciphertext
    ciphertext = read_file(path)
    ciphertext = normalize_text(ciphertext)

    # Solve to find the best key
    key = solve(ciphertext)
    
    # Decrypt using the found key
    plaintext = decrypt_with_key(ciphertext, key)

    # Display result
    print("\nDecrypted text:\n")
    print(plaintext)

    # Save output files
    pt_file = f"output/plaintext/plaintext_{filename}"
    key_file = f"output/keys/key_{filename}"

    with open(pt_file, "w", encoding="utf-8") as f:
        f.write(plaintext)

    with open(key_file, "w", encoding="utf-8") as f:
        for cipher_char, plain_char in key.items():
            f.write(f"{cipher_char} -> {plain_char}\n")

    print("\nSaved:")
    print(" ", pt_file)
    print(" ", key_file)


if __name__ == "__main__":
    main()