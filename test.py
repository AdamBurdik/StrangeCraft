import hashlib

def generate_sha1_hash(data):
    sha1_hash = hashlib.sha1(data.encode()).hexdigest()
    return sha1_hash

# Example usage
data_to_hash = "Hello, World!"
sha1_result = generate_sha1_hash(data_to_hash)

print(f'SHA-1 Hash: {sha1_result}')