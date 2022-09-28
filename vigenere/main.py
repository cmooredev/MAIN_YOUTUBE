def encrypt(plaintext, key):
    result = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = (ord(key[i]) -65)
        result += chr((ord(char) + key_char-65) % 26 + 65)

    return result

plaintext = "HEY"
key = 'BBB'
ciphertext = encrypt(plaintext, key)
print("Plaintext: " + plaintext)
print("Ciphertext: " + ciphertext)

