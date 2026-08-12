def encrypt(text):
    result = ""
    for char in text:
        result += chr(ord(char) + 3)
    return result

def decrypt(text):
    result = ""
    for char in text:
        result += chr(ord(char) - 3)
    return result

text = input("Enter string :")

encrypted = encrypt(text)
print("Encrypted Code is :", encrypted)

decrypted = decrypt(encrypted)
print("Decrypted code is :", decrypted)