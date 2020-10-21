 #Desarrollar cada una de las siguientes funciones y escribir un programa que permita
 #verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
 #a. Cargar un vector con números al azar de cuatro dígitos. La cantidad de elementos
 #también será un número al azar de dos dígitos.
 #b. Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
 #c. Eliminar todas las repeticiones de un valor en la lista anterior. El valor a eliminar
 #se recibe como parámetro.
 #d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
 #auxiliares.

import random

def cargar_vector(vector):
    tamaño = random.randint(10,99)
    #tamaño = random.randint(1,9)
    for i in range(0,tamaño):
        vector.append(random.randint(1,9))

def calcular_suma_vector(vector):
    suma = sum(vector)
    return suma

#def elimino_valor(vector,eliminar):
#   salir = 0
    #while (salir != 1):
        #if eliminar in vector: #me cago en el for uso el IF, IN
        #        vector.remove(eliminar)
        #else:
        #        salir = 1

def elimino_valor(vector,eliminar):
    for i in range(len(vector)):
        if eliminar in vector: #me cago en el for uso el IF, IN
            vector.remove(eliminar)



def es_capicua(vector):
    mitad = len(vector) // 2
    if (mitad == 1):
        if (vector[0] ==[1]):
            result = True
            return result
    for i in range(1,mitad):
        result = False
        count = 1
        if (vector[mitad-count] == vector[mitad+count]):
            result = True
        else:
            result = False
            return result
        count = count + 1
    return result


vector = []
print("Carga de vector")
# --- punto a) --- #
cargar_vector(vector)
print("la lista queda: \n")
print(vector)
# --- punto b) --- #
suma = calcular_suma_vector(vector)
print ("\nla suma de los elementos queda:\n",suma)
# --- punto c()
eliminar = int(input("Ingrese un valor para eliminar las repeticiones \n"))
print(eliminar)
elimino_valor(vector,eliminar)
print("la lista queda: \n")
print(vector)
# --- punt d) --- #
print("Reviso si es capicua...")
if (len(vector) == 1):
    print ("la lista tiene solo un valor")
else:
    result = es_capicua(vector)
    if (result == True):
        print("Es capicua!")
    else:
        print("No es capicua")
