# main.py
# Entry point for substitution cipher solver

import os
from utils import read_file, normalize_text
from solver import solve, decrypt_with_key


CIPHERTEXT_DIR = "ciphertexts"
PLAINTEXT_OUT = "output/plaintext"
KEY_OUT = "output/keys"


def write_plaintext(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


def write_key(filename, key):
    with open(filename, "w", encoding="utf-8") as f:
        for c, p in key.items():
            f.write(f"{c} -> {p}\n")


def main():
    files = sorted(os.listdir(CIPHERTEXT_DIR))

    for fname in files:
        if not fname.endswith(".txt"):
            continue

        print("\n" + "=" * 60)
        print("Decrypting:", fname)
        print("=" * 60)

        path = os.path.join(CIPHERTEXT_DIR, fname)

        text = read_file(path)
        text = normalize_text(text)

        key = solve(text)
        plaintext = decrypt_with_key(text, key)

        print("\nDecrypted text (first 500 chars):\n")
        print(plaintext[:500])

        # write outputs
        pt_file = os.path.join(
            PLAINTEXT_OUT, f"plaintext_{fname}"
        )
        key_file = os.path.join(
            KEY_OUT, f"key_{fname}"
        )

        write_plaintext(pt_file, plaintext)
        write_key(key_file, key)

        print("\nSaved:")
        print(" ", pt_file)
        print(" ", key_file)


if __name__ == "__main__":
    main()
