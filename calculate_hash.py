import hashlib
import sys

def calculate_hash(content):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(content.encode('utf-8'))
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    content = sys.stdin.read()
    print(calculate_hash(content))
