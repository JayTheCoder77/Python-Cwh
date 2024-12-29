# cypher program encryption
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()
random.shuffle(key)
# print(f"chars : {chars}")
# print(f"key   : {key}")

plain_text = input("enter string")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"cipher_text is {cipher_text} from the og message : {plain_text}")


# decrypt

cipher_text = input("enter string to decrypt")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"plain_text is {plain_text} from the encrypted message after decryption : {cipher_text}")