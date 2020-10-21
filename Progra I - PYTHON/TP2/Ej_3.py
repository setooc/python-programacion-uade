#3. Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
#donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores
#de la lista, utilizando la técnica de las rebanandas.
import random

def cargar_lista(lista,n):
    for i in range(n):
        lista.append(i+1)
        print(lista)
        lista[i] = lista[i] ** 2

lista = []
print("Carga de la lista")
n = int(input("Ingrese hasta que numero quiere saber el cuadrado: "))
cargar_lista(lista,n)
print("la lista queda: \n")
print(lista)
print(n)
lista_cortada = []
#for i in range(n-1,1,-1):
n = n-1
count = 0
while (count!=10):
    lista_cortada.append(lista[n])
    n = n - 1
    count += 1
print("Lista cortada queda: \n")
print(lista_cortada)
