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
    
    "Matriz resultante"
    final = np.zeros((int(np.shape(mat)[0]), int(np.shape(mat)[1])), dtype = int)

    "Inicializacion de ciclos"
    num1 = 0
    for i in range (np.shape(mat)[0] - np.shape(kernel)[0] + 1):
        for j in range (np.shape(mat)[1] - np.shape(kernel)[1] + 1):
            "Se obtiene la matriz del producto punto"
            num1 += np.multiply((mat[i:i + (np.shape(kernel)[0]),
                                     j:j + (np.shape(kernel)[1])]), kernel)
            "Se coloca la suma de estos valores en la matriz resultante"
            final[i + m][j + n] = num1.sum()
            "Se repite el proceso asignando el cero a la valor de la variable"
            num1 = 0
    "Matriz resultante"
    plt.imshow(final, cmap='gray')
    plt.title("Imagen usando Kernel")
    plt.show()
