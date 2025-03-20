from PIL import Image
import numpy as np
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt_ECB(image_path, key):
    img = Image.open(image_path)
    img_data = np.array(img)
    img_bytes = img_data.tobytes()
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_bytes = cipher.encrypt(pad(img_bytes, AES.block_size))
    encrypted_array = np.frombuffer(encrypted_bytes[:img_data.size], dtype=np.uint8).reshape(img_data.shape)

    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.show()

def encrypt_CBC(image_path, key):
    img = Image.open(image_path)
    img_data = np.array(img)
    img_bytes = img_data.tobytes()

    iv = get_random_bytes(16)  
    cipher = AES.new(key, AES.MODE_CBC, iv)

    encrypted_bytes = cipher.encrypt(pad(img_bytes, AES.block_size))
    encrypted_array = np.frombuffer(encrypted_bytes[:img_data.size], dtype=np.uint8).reshape(img_data.shape)

    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.show()

# Cargar una imagen
key = get_random_bytes(32)
# file_path = r"Ejemplos/examples/3.simetricos/block/modes_ecb_cbc/canal_inseguro.png"
file_path = r"Ejemplos/examples/3.simetricos/block/modes_ecb_cbc/pic_robot.png"
encrypt_ECB(file_path, key)  # Modo ECB
encrypt_CBC(file_path, key)  # Modo CBC