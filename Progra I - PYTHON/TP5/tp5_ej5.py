# El método index permite buscar un elemento dentro de una lista, devolviendo la
# posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
# produce una excepción de tipo ValueError. Desarrollar un programa que cargue
# una lista con elementos y permita que el usuario busque la posición que ocupa alguno
# de ellos utilizando el método index. Si el elemento no pertenece a la lista se
# imprimirá un mensaje de error y se solicitará un nuevo elemento para buscar. No
# utilizar el operador in.

def cargar_lista(lista):
    elemento = 0
    while (elemento != "q"):
        elemento = input("Ingrese un elemento para la lista, ""q para terminar"" \n")
        if(elemento == "q" or elemento == "Q"):
            print("Se termino la carga de la lista")
            print("La lista queda: \n")
            print(lista)
            elemento = "q"
        else:
            lista.append(elemento)

def busca_elemento(lista,n):
    try:
        valor = lista.index(n)
        print("Encontre {} en la posicion {} ".format(n,valor))
    except (ValueError):
        print("No se encontro el valor en la lista \n")

#MAIN

lista = []
print("Vamos a cargar una lista de elementos \n ")
cargar_lista(lista)
valor = 0
while (valor != "q"):
    valor = input("Ingrese el valor que desea buscar")
    busca_elemento(lista,valor)
