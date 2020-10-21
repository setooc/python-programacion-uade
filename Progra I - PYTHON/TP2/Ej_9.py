#Escribir una función que reciba una lista de números enteros como parámetro y la
#normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones
#relativas que cada elemento tiene en la lista original. Desarrollar también
#un programa que permita verificar el comportamiento de la función. Por ejemplo,
#normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].

import random

def cargar_lista(lista,n,suma):
    tamaño = int(n)
    for i in range(0,n):
        lista.append(random.randint(1,100))
        suma += lista[i]
    return suma

def normalizar_lista(lista,n,suma):
    total = 0
    for i in range(n):
        valor=lista[i] / suma
        lista.insert(i,valor)
        lista.pop(i+1)
        total=total + lista[i]
    return total

lista = []
suma = 0
n = int(input("ingrese el tamaño de la lista: "))
suma = cargar_lista(lista,n,suma)
print ("la lista queda: ",lista)
print("Normalizando lista")
suma = normalizar_lista(lista,n,suma)
print(lista)
print("la suma debe dar 1 \n",suma)
