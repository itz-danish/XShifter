# XShifter Encryption Program

# Extend key_map to cover the full range (0-255)
key_map = {chr(i): (i % 127) + 1 for i in range(256)}

def string_to_binary_string(text):
    """Convert a string to a binary string representation"""
    return ''.join(format(ord(c), '08b') for c in text)

def xor_xshifter(binary_data, binary_key):
    """Perform XOR encryption (same function works for decryption)"""
    key_repeated = (binary_key * ((len(binary_data) // len(binary_key)) + 1))[:len(binary_data)]
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(binary_data, key_repeated))

def swap_xshifter(key_map, binary_encrypted_data, binary_key):
    """Swap the binary data based on key values"""
    max_len = len(binary_encrypted_data)
    key = ''.join(chr(int(binary_key[i:i+8], 2)) for i in range(0, len(binary_key), 8))  # Convert binary key to text
    swapped_value = binary_encrypted_data

    for i in range(min(len(key), max_len)):
        char = key[i]
        split_index = key_map.get(char, ord(char) % max_len) % max_len  # Ensure valid split index

        if 0 < split_index < max_len:
            swapped_value = swapped_value[split_index:] + swapped_value[:split_index]  # Swap

    return swapped_value

def xshifter_encrypt(plain_text, key, key_map):
    """Encrypt a plaintext string using XOR and swapping"""
    if not plain_text or not key:
        raise ValueError("Text and key cannot be empty!")

    binary_data = string_to_binary_string(plain_text)
    binary_key = string_to_binary_string(key)

    xor_enc = xor_xshifter(binary_data, binary_key)
    final_encrypted_value = swap_xshifter(key_map, xor_enc, binary_key)

    return final_encrypted_value

# Example usage
if __name__ == "__main__":
    plain_text = input("Enter text to encrypt: ")
    key = input("Enter encryption key: ")

    encrypted_text = xshifter_encrypt(plain_text, key, key_map)
    print("\nEncrypted Binary:", encrypted_text)
