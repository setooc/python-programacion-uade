def concatenar_numero (num1, num2):
    aux = num2
    count = 0
    while (aux > 1):
        aux = aux /10
        count = count + 1
    num1 = num1 * (10**count)
    num = num1 + num2
    return num


num1 = int(input("ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = concatenar_numero(num1, num2)
print(num1)
print(num2)
print(num3)
