# Desarrollar una función que reciba tres números enteros positivos y verifique si
# corresponden a una fecha gregoriana válida (día, mes, año). Devolver True o False
# según la fecha sea correcta o no. Realizar también un programa para verificar el
# comportamiento de la función.
# Año biciesto
# p: Es divisible entre 4 q: Es divisible entre 100 r: Es divisible entre 400
# La condicion entonces es p and (no q O r) es biciesto tengo 29 dias
# Debugger: ejecutamos como >py -m pdb Ej2.py
# tiramos n para siguiente linea y s para meternos en la funcion

def verificar_fecha (d,m,a):
    if (a<0 or a>9999):
        return -1
    if (m>12 or m<1):
        return -1
    #if not ((d==29 and m==2 and a % 4 == 0) and (a % 100 != 0 or a % 400 == 0)):
    if (d==29 and m==2 and a % 4 == 0):
        if (a % 100 != 0 or a % 400 == 0):
            return 1
    if (( m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and d>31 ): # estos tienen 31 dias
        return -1
    if (( m==4 or m==6 or m==9 or m==11) and d>30 ): # estos tienen 30 dias
        return -1
    return 1

print("ingresemos una fecha: _ / _ / _")
d = int(input("ingrese el dia: "))#29
print("ingresemos una fecha: dia / _ / _")
m = int(input("ingrese el mes: "))#2
print("ingresemos una fecha: dia / mes / _")
a = int(input("ingrese el año: "))#1956
print("ingresemos una fecha: dia / mes / año")
result = verificar_fecha(d,m,a)
if (result < 0):
    print("la Fecha es incorrecta")
if (result > 0):
    print("la Fecha es correcta")
