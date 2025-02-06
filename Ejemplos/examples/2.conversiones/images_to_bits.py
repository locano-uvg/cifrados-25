from PIL import Image  # pip install pillow
import numpy as np


def image_to_bit_array(image_path_original):
    # Abrir las imágenes
    original_image = Image.open(image_path_original)
    # Convertir imágenes a escala de grises y arrays de NumPy
    original_array = np.array(original_image)  # Convertir a escala de grises


def bit_array_to_image(original_array, output_path):
    # Crear una nueva imagen a partir del array resultante
    n_image = Image.fromarray(original_array.astype(np.uint8))
    # Guardar la imagen resultante
    n_image.save(output_path)
    print(f"Imagen resultante guardada en: {output_path}")


def compare_image_size(original_image, second_image):
    # Convertir imágenes a escala de grises y arrays de NumPy
    original_array = np.array(original_image)  # Convertir a escala de grises
    second_array = np.array(second_image)  # Convertir a escala de grises

    # Verificar si las imágenes tienen el mismo número de canales
    if original_array.shape[2] != second_array.shape[2]:
        raise ValueError("Ambas imágenes deben tener el mismo número de canales.")


# Ejemplo de uso
image_path_original = r"Ejemplos/labs/lab2/assets/imagen3.jpg"
output_path = r"Ejemplos/labs/lab2/assets/imagen3_v2.jpg"
