#Eliminar de una lista de palabras las palabras que se encuentren en una segunda
#lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.


import time
import sys


def eliminar_palabras_clave(lista,lista_clave,lista_nueva):
    for i in range(len(lista)):
        for j in range(len(lista_clave)):
            if not lista[i] in lista_clave[j]:
                lista_nueva.append(lista[i])

lista = []
valor = "a"
while (valor != "q"):
    valor = input("Ingrese una palabra en la lista: 'q' para terminar"" \n")
    if (valor == "q"):
        print("Se termina la carga de la lista de palabras")
        print("\n")
        print(lista)
    else:
        lista.append(valor)
        print(lista)

lista_clave = []
valor = "a"
while (valor != "q"):
    valor = input("Ingrese palabras claves en la lista: 'q' para terminar"" \n")
    if (valor == "q"):
        print("Se termina la carga de la lista de palabras")
        print("\n")
        print(lista_clave)
    else:
        lista_clave.append(valor)
        print(lista_clave)
lista_nueva = []
toolbar_width = 10
# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()
sys.stdout.write("\n")
eliminar_palabras_clave(lista,lista_clave,lista_nueva)
print("La lista original es: ", lista)
print("La lista con palabras claves es: ", lista_clave)
print("La lista nueva: ", lista_nueva)
