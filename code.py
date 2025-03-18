# problem 5
def decrypt(ciphertext, key):
    plaintext = ""
    for character in ciphertext:
        if character.isalpha():
            shift = (ord(character) - ord('A') - key) % 26
            plaintext += chr(shift + ord('A'))
        else:
            plaintext += character
    return plaintext

ciphertext = "BEEAKFYDIXUQYHYJIQRYHTYoIQFBQDUYIIIKFUHCQD"

print("ciphertext:", ciphertext)
print("\nTrying all keys (0-25):\n")

for key in range(26):
    decrypted_text = decrypt(ciphertext, key)
    print(f"Key {key:2d}: {decrypted_text}")
