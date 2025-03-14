# XShifter Decryption Program

# Extend key_map to cover the full range (0-255)
key_map = {chr(i): (i % 127) + 1 for i in range(256)}

def binary_to_string(binary_string):
    """Convert a binary string back to a text string"""
    return ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))

def string_to_binary_string(text):
    """Convert a string to a binary string representation"""
    return ''.join(format(ord(c), '08b') for c in text)

def xor_xshifter(binary_data, binary_key):
    """Perform XOR encryption (same function works for decryption)"""
    key_repeated = (binary_key * ((len(binary_data) // len(binary_key)) + 1))[:len(binary_data)]
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(binary_data, key_repeated))

def swap_back_xshifter(key_map, binary_encrypted_data, binary_key):
    """Reverse the swap operation"""
    max_len = len(binary_encrypted_data)
    key = binary_to_string(binary_key)  # Convert binary key to text
    swapped_value = binary_encrypted_data

    for i in reversed(range(min(len(key), max_len))):
        char = key[i]
        split_index = key_map.get(char, ord(char) % max_len) % max_len  # Ensure valid split index

        if 0 < split_index < max_len:
            swapped_value = swapped_value[-split_index:] + swapped_value[:-split_index]  # Reverse swap

    return swapped_value

def xshifter_decrypt(encrypted_text, key, key_map):
    """Decrypt an encrypted binary string using reverse swapping and XOR"""
    if not encrypted_text or not key:
        raise ValueError("Encrypted text and key cannot be empty!")

    binary_key = string_to_binary_string(key)

    swapped_binary = swap_back_xshifter(key_map, encrypted_text, binary_key)
    decrypted_binary = xor_xshifter(swapped_binary, binary_key)

    original_text = binary_to_string(decrypted_binary)

    return original_text

# Example usage
if __name__ == "__main__":
    encrypted_text = input("Enter binary to decrypt: ")
    key = input("Enter decryption key: ")

    decrypted_text = xshifter_decrypt(encrypted_text, key, key_map)
    print("\nDecrypted Text:", decrypted_text)
