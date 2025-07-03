import hashlib

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

if __name__ == "__main__":
    file_path = "D:\\jarvis\\Jarvis\\conversation_log.md"
    # Read the file to remove the old hash
    with open(file_path, "r") as f:
        lines = f.readlines()
    # Find the line with the old hash
    for i, line in enumerate(lines):
        if "SHA256 Hash" in line:
            lines = lines[:i-2]
            break
    # Write the file without the old hash
    with open(file_path, "w") as f:
        f.writelines(lines)

    file_hash = calculate_hash(file_path)
    with open(file_path, "a") as f:
        f.write(f"\n\n---\n**SHA256 Hash:** {file_hash}")

