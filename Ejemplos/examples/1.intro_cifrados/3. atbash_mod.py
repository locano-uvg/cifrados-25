
alphabet = "abcdefghijklmnñopqrstuvwxyz"

# Encript: E(x) = (x + n) mod 26
#  x = letter index
#  n = length of the alphabet
# Decript: D(x) = (x - n) mod 26

def encript(plain_text): 
    cipher_text = ""

    for c in plain_text:
        if c in alphabet:
            x = alphabet.index(c)
            y = len(alphabet) -1 
            v = x +y
            g = len(alphabet)
            b = v % g
            cipher_text += alphabet[(alphabet.index(c) + (len(alphabet)-1)) % len(alphabet)]
        else:
            cipher_text += c

    return cipher_text

def decript(cipher_text):
    plain_text = ""

    for c in cipher_text:
        if c in alphabet:     
            plain_text += alphabet[(alphabet.index(c) - (len(alphabet)-1)) % len(alphabet)]
        else:
            plain_text += c

    return plain_text       

print("ENCRIPTION:")
plain_text = input("Enter your message: ")
print("Encrypted:", encript(plain_text))

print("___________________\n")

print("DECRIPTION:")
cipher_text = input("Enter the cipher text to decript: ")
print("Decrypted:", decript(cipher_text))