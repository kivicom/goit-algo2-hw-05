import hashlib
import math

class BloomFilter:
    def __init__(self, size, num_hashes):
        # Initialize the bit array with zeros
        self.size = size
        self.bit_array = [0] * size
        self.num_hashes = num_hashes

    def _hashes(self, item):
        # Generate multiple hash values for the item
        item_str = str(item)  # Convert to string to handle any type
        hashes = []
        for i in range(self.num_hashes):
            # Use different seeds for each hash function
            hash_obj = hashlib.md5((item_str + str(i)).encode('utf-8'))
            hash_value = int(hash_obj.hexdigest(), 16) % self.size
            hashes.append(hash_value)
        return hashes

    def add(self, item):
        # Add an item to the Bloom filter
        if item is None or item == "":
            raise ValueError("Item cannot be None or empty")
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def check(self, item):
        # Check if an item might be in the Bloom filter
        if item is None or item == "":
            raise ValueError("Item cannot be None or empty")
        for hash_value in self._hashes(item):
            if self.bit_array[hash_value] == 0:
                return False
        return True

def check_password_uniqueness(bloom_filter, passwords):
    # Check uniqueness of passwords using the Bloom filter
    results = {}
    for password in passwords:
        if not isinstance(password, str) or password == "":
            results[password] = "invalid input"
            continue
        if bloom_filter.check(password):
            results[password] = "already used"
        else:
            results[password] = "unique"
            bloom_filter.add(password)  # Add new password to filter
    return results

if __name__ == "__main__":
    # Initialize Bloom filter
    bloom = BloomFilter(size=1000, num_hashes=3)

    # Add existing passwords
    existing_passwords = ["password123", "admin123", "qwerty123"]
    for password in existing_passwords:
        bloom.add(password)

    # Check new passwords
    new_passwords_to_check = ["password123", "newpassword", "admin123", "guest"]
    results = check_password_uniqueness(bloom, new_passwords_to_check)

    # Print results
    for password, status in results.items():
        print(f"Пароль '{password}' — {status}.")
