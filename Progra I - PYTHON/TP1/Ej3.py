# Para un número entero N menor de 100 recibido como parámetro, escribir un programa
# que utilice una función para devolver la suma de los cuadrados de aquellos
# números entre 1 y N que están separados entre si por cuatro unidades. (1^2 + 5^2 +9^2 + 13^2 + …)

def calcula_suma_cuadrado (n):
    suma = 0
    for i in range(1,n+1,4): #salto de 4 en 4
        # print(i) # para debug
        suma = suma + (i**2)
        # print(suma) # para debug
    return suma

n = int(input("Ingrese un numero n hasta 100, para sumar los cuadrados: "))
while ( n >100):
    n = int(input("Ingrese un numero n hasta 100, para sumar los cuadrados: "))
print("la suma queda: ", calcula_suma_cuadrado (n))
