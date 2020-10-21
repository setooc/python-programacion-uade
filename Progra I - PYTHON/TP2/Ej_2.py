#Escribir funciones para:
#a. Recibir una lista como parámetro y devolver True si la misma contiene algún
#elemento repetido. La función no debe modificar la lista.
#b. Generar una lista de 50 números aleatorios del 1 al 100 y comprobar con la
#función anterior si existen elementos duplicados. Devolver True o False.
#c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
#únicos de la lista original, sin importar el orden.
import random

def cargar_lista(lista):
    #tamaño = random.randint(1,9)
    tamaño = 50
    for i in range(0,tamaño):
        lista.append(random.randint(1,100))


def elemento_repetido (lista):
    for i in range(len(lista)):
        repe = lista.count(lista[i])
        print (repe)
        if (repe > 1):
            return True
    return False

def nueva_lista(lista):
    lista2 = []
    for i in range(len(lista)):
        repe = lista.count(lista[i])
        print ("Repe = ",repe)
        if (repe == 1):
            print("valor nueva lista: ",lista[i])
            lista2.append(lista[i])
    return lista2


# --- Main --- #
lista = []
print("Carga de la lista")
cargar_lista(lista)
print("la lista queda: \n")
print(lista)
# --- punto a) --- #
print("Tenemos elementos repetidos en la lista ?")
valor = elemento_repetido(lista)
if (valor):
    print("tenemos valores repetidos")
else:
    print("no hay valores repetidos en la lista ")
# --- punto c) --- #
print ("Generamos una nueva lista con los elementos unicos de la anterior...")
lista2 = nueva_lista(lista)
print("la nueva lista queda: \n")
print(lista2)
