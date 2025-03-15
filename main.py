import hashlib

def crack_hash(hash_to_crack, wordlist_file, hash_type="md5"):
    """Attempts to crack a given hash using a wordlist."""
    try:
        with open(wordlist_file, "r", encoding="utf-8") as file:
            for word in file:
                word = word.strip()
                hashed_word = hashlib.new(hash_type, word.encode()).hexdigest()
                
                if hashed_word == hash_to_crack:
                    print(f"[+] Password Found: {word}")
                    return

        print("[-] Password not found in wordlist.")

    except FileNotFoundError:
        print("[-] Wordlist file not found.")

if __name__ == "__main__":
    hash_input = input("Enter hash to crack: ")
    wordlist_path = input("Enter path to wordlist: ")
    hash_algorithm = input("Enter hash type (md5, sha1, sha256, etc.): ").lower()

    crack_hash(hash_input, wordlist_path, hash_algorithm)
