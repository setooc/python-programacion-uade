#3. Desarrollar un programa para rellenar una matriz de N x N con números enteros al
#azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita.
#Imprimir la matriz por pantalla.

import random

def crear_matriz(dimen):
    matriz = [[0] * dimen for i in range(dimen)]
    print(matriz)
    return matriz

def mostrar_matriz(matriz):
    dimen = len(matriz)
    for f in range(dimen):
        for c in range(dimen):
            print("%3d" %matriz[f][c], end="")
        print()


def llenar_matriz(matriz):
    dimen = len(matriz)
    ultimo = dimen ** 2
    repe = 0
    lista_repe = []
    for f in range(dimen):
        for c in range (dimen):
            numero = (random.randint(0,ultimo))
            while numero in lista_repe:
                numero = (random.randint(0,ultimo))
            matriz[f][c] = numero
            lista_repe.append(numero)

# ---- Main ----- #
matriz = []
print("Generamos la matriz NxN")
dimen = int(input("Ingrese la dimension de la matriz cuadrada \n"))
#matriz = [[0] * columnas for i in range(filas)]
# --- Genero la matriz --- #
print("Creando matriz completa con ceros")
matriz = crear_matriz(dimen)
mostrar_matriz(matriz)

print("Llenar la matriz con valores aleatorios...")
llenar_matriz(matriz)

# --- Muestro la matriz con valores aleatorios --- #
mostrar_matriz(matriz)
