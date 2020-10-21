#4. Definir una función superposición() que reciba como parámetros dos listas de cualquier
#tipo y devuelva True si tienen al menos un elemento en común, o False en
#caso contrario. Desarrollar un programa para verificar su comportamiento.
import time
def superposicion(lista,lista2):
    for i in range(len(lista)):
        for j in range(len(lista2)):
            print(lista[i])
            print(lista2[j])
            if lista[i] in lista2[j]:
                print(lista[i])
                print(lista2[j])
                return True
    return False

lista = []
valor = "a"
while (valor != "q"):
    valor = input("Ingrese un elemento a la lista: ""q"" para terminar"" \n")
    if (valor == "q"):
        print("Se termina la carga de la lista 1")
        print("*"*60)
        print(lista)
    else:
        lista.append(valor)
        print(lista)
lista2 = []
valor = "a"
while (valor != "q"):
    valor = input("Ingrese un elemento a la lista2: ""q"" para terminar"" \n")
    if (valor == "q"):
        print("Se termina la carga de la lista 2")
        print("*"*60)
        print(lista2)
    else:
        lista2.append(valor)
        print(lista2)
print(lista)
print(lista2)
print("Revisar valores")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
result = superposicion(lista,lista2)
if (result == True):
    print("Las listas tienen al menos un valor en comun")
else:
    print("Las listas no tienen valores en comun")
