def encrypt(text):
    result = " "
    for char in text:
        result += chr(ord(char) + 3)
        return result

def decrypt(text):
    result = " "
    for char in text:
        result += char(ord(char) - 3)
        return result

string = int(input("Enter the string :"))

encrypted = encrypt(string)
print("Encrypted String is : ",encrypted)

decrypted = decrypt(string)
print("Decrypted String is :",decrypt)
