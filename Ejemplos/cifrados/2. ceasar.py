
alphabet = "abcdefghijklmnñopqrstuvwxyz"

def encript(plain_text, key): 
    cipher_text = ""

    for c in plain_text:
        if c in alphabet:
            # We get the index of the letter in the alphabet
            # and add the key to it. Then we get the remainder
            # of the division of the sum and the length of the
            # alphabet. This is done to avoid getting an index
            # that is out of range.
            cipher_text += alphabet[(alphabet.index(c) + key) % len(alphabet)]
        else:
            cipher_text += c

    return cipher_text

def decript(cipher_text, key):
    plain_text = ""

    for c in cipher_text:
        if c in alphabet:
            # We get the index of the letter in the alphabet
            # and subtract the key to it. Then we get the remainder
            # of the division of the difference and the length of the
            # alphabet. This is done to avoid getting an index
            # that is out of range.
            plain_text += alphabet[(alphabet.index(c) - key) % len(alphabet)]
        else:
            plain_text += c

    return plain_text       


# Encript: E(x) = (x + k) mod n
#  x = letter index
#  k = key
#  n = length of the alphabet
# Decript: D(x) = (x - k) mod n


# print("ENCRIPTION:")
# plain_text = input("Enter your message: ")
# k = int(input("Enter the key encript: "))
# cipher_text = encript(plain_text, k)

# print("Encrypted:", cipher_text) 

# print("___________________\n")

# print("DECRIPTION:") 
# cipher_text = input("Enter the cipher text to decript: ")
# k = int(input("Enter the key to decript: "))

# print("Decrypted:", decript(cipher_text, k))