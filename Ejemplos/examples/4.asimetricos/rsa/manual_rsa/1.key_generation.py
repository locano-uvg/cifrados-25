import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def is_prime(n):
    # Función para verificar si un número es primo
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_random_prime():
    # Función para generar un número primo aleatorio
    prime_candidate = random.randint(100, 500)
    while not is_prime(prime_candidate):
        prime_candidate = random.randint(100, 500)
    return prime_candidate

def generate_rsa_keys():
    # Genera dos números primos aleatorios para p y q
    p = generate_random_prime()
    q = generate_random_prime()

    # Calcula n y (p-1)*(q-1)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Elige un exponente de cifrado e que sea coprimo con phi
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Calcula el exponente de descifrado d usando inverso multiplicativo modular
    d = modinv(e, phi)

    # Devuelve las claves pública y privada
    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key

# Ejemplo
public_key, private_key = generate_rsa_keys()

# Muestra las claves generadas
print("Clave Pública (n, e):", public_key)
print("Clave Privada (n, d):", private_key)