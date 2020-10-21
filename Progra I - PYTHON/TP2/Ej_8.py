#Generar dos listas con M y N números al azar entre 1 y 50 y construir una tercera
#lista cuyos elementos sean el resultado de la intersección de las dos listas dadas.
#Los valores de M y N se obtienen al azar. Imprimir las tres listas por pantalla.

import random


def cargar_lista(lista):
    tamaño = 5
    for i in range(0,tamaño):
        lista.append(random.randint(1,10))

def comparar_listas(listaA,listaB):
    for i in range(len(listaA)):
        for j in range(len(listaB)):
            if (listaA[i] == listaB[j]):
                repe = listaC.count(listaB[j])
                if (repe == 0):
                    listaC.append(listaB[j])

listaA=[]
listaB=[]
print("Cargando lista A: ")
cargar_lista(listaA)
print("Cargando lista B: ")
cargar_lista(listaB)
print("La lista A resulta: ", listaA)
print("La lista B resulta: ", listaB)
print("Comparamos listas...")
listaC = []
comparar_listas(listaA,listaB)
print("la lista interseccion resulta: \n")
print(listaC)
