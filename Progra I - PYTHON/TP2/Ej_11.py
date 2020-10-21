
import random


def cargar_lista(lista):
    #tamaño = random.randint(1,9)
    tamaño = random.randrange(10,50,2)
    for i in range(0,tamaño):
        lista.append(random.randint(1,100))

def intercalar_listas(lista1,lista2):
    for i in range(len(lista1)):
        if(i // 2):
            lista1[i:i]=lista2[i]




lista1 = []
lista2 = []
print("Generando listas")

print("Lista 1:")
cargar_lista(lista1)
print("La lista completa queda: ")
print(lista1)

print("Lista 2:")
cargar_lista(lista2)
print("La lista completa queda: ")
print(lista2)

intercalar_listas(lista1,lista2)
print("La lista resultante es: ")
print(lista1 )
