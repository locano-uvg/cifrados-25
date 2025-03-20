import random
def createKey(size):
    key = []
    for i in range(size):
        key.append(random.randint(0,256))
    return key

def cypherText(text, keystream):
    ciphertext = []
    for i in range(len(text)):
        ciphertext.append(text[i] ^ keystream[i])
    return ciphertext

def decypherText(ciphertext, keystream):
    text = []
    for i in range(len(ciphertext)):
        text.append(ciphertext[i] ^ keystream[i])
    return text

text = input("Introduce el texto a cifrar: ")
text_to_bytes = text.encode()

keystream = createKey(len(text_to_bytes))
keystream = bytes(keystream)

ciphertext = cypherText(text_to_bytes, keystream)
print("Texto cifrado: ", ciphertext)
print("-"*50)

decyphertext = decypherText(ciphertext, keystream)
print("Texto descifrado: ", bytes(decyphertext).decode())
print("-"*50)

