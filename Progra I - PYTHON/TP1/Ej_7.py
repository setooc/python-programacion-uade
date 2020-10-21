# 7. Desarrollar una función que reciba como parámetros dos números enteros y
# devuelva el número que resulte de concatenar ambos valores.
# Por ejemplo, si recibe 1234 y 567 debe devolver 1234567.

def concatenar_numero(num1, num2):
    num3=(num1+num2)
    return num3

num1 = str(input("ingrese un numero: "))
num2 = str(input("ingrese un segundo numero: "))
print("El numero concatenado resulta: ",concatenar_numero(num1, num2))
