# Escribir una función que reciba una lista como parámetro y devuelva True si la lista
# está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
# ordenada([1, 2, 3]) retorna True y ordenada([b, a]) retorna False. Desarrollar además
# un programa para verificar el comportamiento de la función.
import random

def cargar_lista(lista):
    tamaño = random.randint(1,9)
    #tamaño = 50
    for i in range(0,tamaño):
        lista.append(random.randint(1,100))

def ordenar_lista (lista):
    lista.sort()

def ordenado(lista):
    ultimo=len(lista)
    if (ultimo == 1):
        #print("valor en funcion:" ,ultimo)
        return "a"
    for i in range(len(lista)-1):
        if (lista[i] > lista[i+1]):
            return False
    return True

lista = []
print("Cargamos la lista")
cargar_lista(lista)
print("Verificamos que la lista este ordenada")
# ordenar_lista(lista)
print(lista)
valor = ordenado(lista)
#print("valor ",valor)
if (valor == "a"):
    print("la lista tiene un solo elemento")
elif (valor == True):
    print("la lista esta ordenada")
else:
    print("la lista no esta ordenada")
