# Laboratorio_Equipo4

Sobel Edge
Es utilizado para la detección de bordes. Calcula la aproximación al gradiente
de la función de intensidad de una imagen. Para cada resultado de la imagen que
se procesa, el resultado es tanto el vector gradiente correspondiente como la norma
del vector.

(-1, -2, -1)
( 0,  0,  0)
( 1,  2,  1)
 Horizontal


( -1,  0, 1)
( -2,  0, 2)
( -1,  0, 1)
Vertical


Edge detection
Es una tecnica de procesado de imagen la cual busca fronteras entre objetos en
una imagen. Funciona detectando discontinuidades en el brillo de una imagen.

( -1, -1, -1)
( -1,  8, -1)
( -1,  -1,-1)



Se eligieron estos tipos de filtros gracias a la facilidad con la que se pueden 
implementar en el proyecto, ademas de dar resultados notables durante el procesamiento
de la imagen.
El filtro Sobel Edge nos da la oportunidad de aplicar dos matrizes diferentes con las
cuales notar una diferencia en cada una de ellas, aunque sea mínima. Por otro lado, 
el Edge Detection es una matriz con la cual solo se notan los bordes de objetos que 
existen en la imagen, por lo que se puede diferenciar cada uno de los filtros.


Nixon, M. (2012). Sobel Edge Detection - an overview | ScienceDirect Topics. ScienceDirect.
https://www.sciencedirect.com/topics/engineering/sobel-edge-detection

MatLab. (s. f.). Edge Detection. MATLAB & Simulink. Recuperado 7 de mayo de 2021, de 
https://la.mathworks.com/discovery/edge-detection.html