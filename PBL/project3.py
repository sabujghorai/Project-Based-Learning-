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

text = input("Enter the string :")

encrypted = encrypt(text)
print("Encrypted String is : ",encrypted)

decrypted = decrypt(text)
print("Decrypted String is :",decrypted)
