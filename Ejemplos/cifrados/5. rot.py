
alphabet = "abcdefghijklmnñopqrstuvwxyz"

def encript(plain_text): 
    cipher_text = ""

    for c in plain_text:
        if c in alphabet:
            cipher_text += alphabet[(alphabet.index(c) + 13) % len(alphabet)]
        else:
            cipher_text += c

    return cipher_text

def decript(cipher_text):
    plain_text = ""

    for c in cipher_text:
        if c in alphabet:
            plain_text += alphabet[(alphabet.index(c) - 13) % len(alphabet)]
        else:
            plain_text += c

    return plain_text       



print("ENCRIPTION:")
plain_text = input("Enter your message: ")
cipher_text = encript(plain_text)

print("Encrypted:", cipher_text) 

print("___________________\n")

print("DECRIPTION:") 
cipher_text = input("Enter the cipher text to decript: ")

print("Decrypted:", decript(cipher_text))


