import hashlib

# Función para calcular el hash de un archivo
def calcular_hash_archivo(nombre_archivo):
    hash_object = hashlib.sha256()
    with open(nombre_archivo, "rb") as archivo:
        for bloque in iter(lambda: archivo.read(4096), b""):
            hash_object.update(bloque)
    return hash_object.hexdigest()

# Archivo y hash precalculado
archivo =  r'Ejemplos/examples/4.asimetricos/hash/documento_alterado.txt'
hash_precalculado = "29f68526129c28be4a3b01d5a4ff5e5e92ff5a05b697f736fa08101e7cdcd1ad"

# Calcular el hash del archivo
hash_calculado = calcular_hash_archivo(archivo)
print(f"Hash calculado: {hash_calculado}")
# Comparar hashes
if hash_calculado == hash_precalculado:
    print("El archivo es íntegro y no ha sido alterado.")
else:
    print("El archivo puede haber sido alterado o corrompido.")