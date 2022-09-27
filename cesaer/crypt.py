def encrypt(text,s):
    result = ""
       # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        #65 = uppercase A
        result += chr((ord(char) + s-65) % 26 + 65)
    return result
#check the above function
plaintext = "ZABCD"
s = 1
cipher = encrypt(plaintext,s)
print("Plain Text : " + plaintext)
print("Cipher: " + cipher)

