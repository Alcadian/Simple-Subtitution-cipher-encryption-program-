#Subtitution  cipher encryption program for beginners
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

#ENCRYPTING
plain_text = input("Enter A Message To Encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Encrypted Message: {cipher_text}")

#DYCRYPTING
cipher_text = input("Enter Encrypted Text TO Decrypt Message")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print("Decrypted")
print(f"Here Is The Originale Message: {plain_text}")