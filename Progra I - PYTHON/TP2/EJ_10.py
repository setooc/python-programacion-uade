#10. Generar una lista con números al azar entre 0 y 100, donde su cantidad de elementos
#será un número par también obtenido al azar entre 10 y 50. Luego se solicita
#partir la lista por la mitad a través de la técnica de las rebanadas, creando dos
#nuevas listas. Imprimir las tres listas por pantalla.

import random


def cargar_lista(lista):
    #tamaño = random.randint(1,9)
    tamaño = random.randrange(10,50,2)
    for i in range(0,tamaño):
        lista.append(random.randint(1,100))

def partir_listas(lista,listaA,listaB):
    mitad = len(lista) // 2
    listaA.append(lista[:mitad])
    listaB.append(lista[mitad:])


lista = []
listaA = []
listaB = []
print("Generando listas")
cargar_lista(lista)
print("La lista completa queda: ")
print(lista)
print("Partiendo lista por la mitad")
partir_listas(lista,listaA,listaB)
print("Las listas quedan: ")
print("La lista A: ")
print(listaA)
print("La lista B: ")
print(listaB)
