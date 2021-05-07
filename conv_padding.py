#Importar librerías
import numpy as np
import math
import cv2
import matplotlib.pyplot as plt

#Filtro = [[-1 0 1]; [-2 0 2]; [-1 0 1]] y edge

def convolucion (img, kernel):
    #Convierte ambas entradas a matrices con ayuda de numpy
    mat = np.matrix(img)
    kernel = np.matrix(kernel)
    #Obtiene las columnas y renglones a agregar por cada lado de la matriz
    m = math.floor((np.shape(kernel)[0] - 1) / 2)
    n = math.floor((np.shape(kernel)[1] - 1) / 2)
    
    #Crea la matriz resultante, con valores de cero
    final = np.zeros((int(np.shape(mat)[0]), int(np.shape(mat)[1])), dtype = int)

    #Se inicializan ambos ciclos for
    
    num1 = 0
    for i in range (np.shape(mat)[0] - np.shape(kernel)[0] + 1):
        for j in range (np.shape(mat)[1] - np.shape(kernel)[1] + 1):
            #Se obtiene la matriz del producto punto
            num1 += np.multiply((mat[i:i + (np.shape(kernel)[0]),
                                     j:j + (np.shape(kernel)[1])]), kernel)
            #Se coloca la suma de estos valores en la matriz resultante
            final[i + m][j + n] = num1.sum()
            #Se le asigna el valor de cero a la variable, para repetir el proceso
            num1 = 0
    #Se imprime la matriz resultante
    plt.imshow(final, cmap='gray')
    plt.title("Imagen usando Kernel con Padding")
    plt.show()

opcion=input("elige filtro 1 o 2: ")
imagen = input('Nombre archivo ')
img = cv2.imread(imagen, cv2.IMREAD_GRAYSCALE)


while opcion==1:
    kernel = '[[-1 0 1]; [-2 0 2]; [-1 0 1]]'

else:
    kernel = '[[-1 -1 -1]; [-1 8 -1]; [-1 -1 -1]]'
    
#Llama a la función, mandando ambas matrices
convolucion(img, kernel)

