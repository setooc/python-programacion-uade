#Escribir un programa que calcule la suma acumulada a partir de una lista de números.
#El programa debe generar una nueva lista donde el primer elemento es el mismo
#de la lista original, el segundo elemento es la suma del primero más el segundo,
#el tercer elemento es la suma del primero más el segundo más el tercero y así
#sucesivamente. Por ejemplo, la suma acumulada de [1,2,3] es [1,3,6].
import random

def cargar_lista(lista,lista_suma):
    tamaño = 10
    suma=0
    for i in range(0,tamaño):
        lista.append(random.randint(1,10))
        suma += lista[i]
        lista_suma.append(suma)

lista = []
lista_suma = []
print("Generamos la primer lista al azar")
cargar_lista(lista,lista_suma)
print(lista)
print("La lista suma queda")
print(lista_suma)
