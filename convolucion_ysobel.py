"Se importan las libreias necesarias"
import numpy as np
import math
import cv2
import matplotlib.pyplot as plt

"Herramientas a utilizar"
"Nombre del archivo = foto.jpeg"
"Filtro = [[-1 0 1]; [-2 0 2]; [-1 0 1]] y vertical sobel edge"

def convolucion (img, kernel):
    "Se convierten las entradas a matrices con numpy"
    mat = np.matrix(img)
    kernel = np.matrix(kernel)
    "Dimensiones de la matriz resultante"
    m = math.floor((np.shape(kernel)[0] - 1) / 2)
    n = math.floor((np.shape(kernel)[1] - 1) / 2)
    
