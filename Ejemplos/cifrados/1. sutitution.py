
alphabet = "abcdefghijklmnñopqrstuvwxyz"
sustitution_alphabet = "pqwertyuiasdfghjklñzxcvbnmo"

def encript(plain_text):
    cipher_text = ""

    for c in plain_text:
        if c in alphabet:
            cipher_text += sustitution_alphabet[alphabet.index(c)]
        else:
            cipher_text += c

    return cipher_text

def decript(cipher_text):
    plain_text = ""

    for c in cipher_text:
        if c in sustitution_alphabet:
            plain_text += alphabet[sustitution_alphabet.index(c)]
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