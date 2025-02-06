

def encriptarXOR(mensaje, clave):
    mensaje = mensaje.encode('utf-8')
    clave = clave.encode('utf-8')
    mensaje_encriptado = bytearray()
    for i in range(len(mensaje)):
        mensaje_encriptado.append(mensaje[i] ^ clave[i % len(clave)])
    return mensaje_encriptado

def desencriptarXOR(mensaje_encriptado, clave):
    mensaje_desencriptado = bytearray()
    for i in range(len(mensaje_encriptado)):
        mensaje_desencriptado.append(mensaje_encriptado[i] ^ clave[i % len(clave)])
    return mensaje_desencriptado.decode('utf-8')

mensaje = input('Ingrese el mensaje a encriptar: ')
clave = input('Ingrese la clave: ')
mensaje_encriptado = encriptarXOR(mensaje, clave)
print(mensaje_encriptado)
mensaje_desencriptado = desencriptarXOR(mensaje_encriptado, clave)
print(mensaje_desencriptado)