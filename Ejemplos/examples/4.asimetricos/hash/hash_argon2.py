from argon2 import PasswordHasher

ph = PasswordHasher()
hash_contraseña = ph.hash("mi_super_contraseña")
print("Hash Argon2:", hash_contraseña)