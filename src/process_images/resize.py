import cv2
import numpy as np
import imutils
import os

# Directorio de entrada y salida
input_dir = "ruta con todas las imágenes"
output_dir = "ruta donde dejar las imágenes con resize"

# Recorrer todas las imágenes en el directorio de entrada
for filename in os.listdir(input_dir):
    # Verificar si el archivo es una imagen
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".JPG") or filename.endswith(".jpeg"):
        # Cargar la imagen utilizando OpenCV
        image_path = os.path.join(input_dir, filename)
        image = cv2.imread(image_path)
        
        # Redimensionar la imagen utilizando imutils
        # Recordar que el programa que entrena las imágenes acepta tamaños pequeños, ideal menores de 50 pixeles.
        resized = imutils.resize(image, width=48)
        
        # Guardar la imagen redimensionada en el directorio de salida
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, resized)
