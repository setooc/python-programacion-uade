#3. Desarrollar un programa para rellenar una matriz de N x N con números enteros al
#azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita.
#Imprimir la matriz por pantalla.

import random

def crear_matriz(filas,columnas):
    matriz = [[0] * columnas for i in range(filas)]
    print(matriz)
    return matriz          # Si no recibe como parametro la matriz la tengo que devolver

def mostrar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()


def llenar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range (columnas):
            matriz[f][c] = int((random.randint(1,100)))

# ---- Main ----- #
matriz = []
print("Generamos la matriz MxN")
filas = int(input("Ingrese el numero de filas: \n"))
columnas = int(input("Ingrese el numero de columnas: \n"))
#matriz = [[0] * columnas for i in range(filas)]
# --- Genero la matriz --- #
print("Creando matriz completa con ceros")
matriz = crear_matriz(filas,columnas)
mostrar_matriz(matriz)

# --- Completo la matriz --- #
print("Llenar la matriz con valores aleatorios...")
llenar_matriz(matriz)

# --- Muestro la matriz con valores aleatorios --- #
mostrar_matriz(matriz)
