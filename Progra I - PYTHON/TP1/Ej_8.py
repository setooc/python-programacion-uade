# Ejercicio 8
# Escribir una función que reciba como parámetro número del 1 al 9 y devuelva
# el resultado de sumar n + nn + nnn + nnnn, donde n corresponde al número recibido.
# Por ejemplo, si se ingresa 3 debe devolver 3702 (3+33+333+3333).
# Escribir también un programa para verificar el comportamiento de la función.

def sumar_num(num):
    print("Primer numero: ", num)
    num2 = num * 11
    print("Segundo numero: ",num2)
    num3 = num * 111
    print("Tercer numero: ",num3)
    num4 = num * 1111
    print("Cuarto numero: ",num4)
    suma = num + num2 +num3 + num4
    return suma

num = 0
while(num<1 or num>9):
    num = int(input("Ingrese un numero del 1 al 9: "))
resul = sumar_num (num)
print("El resultado sera: ", resul)
