# main.py
# Run solver for a single ciphertext file

import sys
import os
from utils import read_file, normalize_text
from solver import solve, decrypt_with_key


def main():
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

    text = read_file(path)
    text = normalize_text(text)

    key = solve(text)
    plaintext = decrypt_with_key(text, key)

    print("\nDecrypted text:\n")
    print(plaintext)

    # save output
    pt_file = f"output/plaintext/plaintext_{filename}"
    key_file = f"output/keys/key_{filename}"

    with open(pt_file, "w", encoding="utf-8") as f:
        f.write(plaintext)

    with open(key_file, "w", encoding="utf-8") as f:
        for c, p in key.items():
            f.write(f"{c} -> {p}\n")

    print("\nSaved:")
    print(" ", pt_file)
    print(" ", key_file)


if __name__ == "__main__":
    main()
