# Ejercicio 9
# Escribir una función diasiguiente(…) que reciba como parámetro una fecha cualquiera
# expresada por tres enteros (correspondientes al día, mes y año) y calcule y
# devuelva tres enteros correspondientes el día siguiente al dado.
# Utilizando esta función, desarrollar programas que permitan:
# a. Sumar N días a una fecha.
# b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.

import time

def verificar_fecha (d,m,a):
    if (a<0 or a>9999):
        return -1
    if (m>12 or m<1):
        return -1
    #if not ((d==29 and m==2 and a % 4 == 0) and (a % 100 != 0 or a % 400 == 0)):
    if (d==29 and m==2 and a % 4 == 0):
        if (a % 100 != 0 or a % 400 == 0):
            print("Es bisiesto!! +1 al dia")
            return 1
    if (( m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and d>31 ): # estos tienen 31 dias
        return -1
    if (( m==4 or m==6 or m==9 or m==11) and d>30 ): # estos tienen 30 dias
        return -1
    return 1

def diasiguiente(d,m,a):
    if (( m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and (d==31) ):
        d = 1
        if (m == 12):
            m = 1
            a = a + 1
            #return d, m, a
        m = m + 1
    elif (( m==4 or m==6 or m==9 or m==11) and d==30 ):
        d = 1
        m = m + 1
    elif ((d==28 and m==2 and a % 4 == 0) and (a % 100 != 0 or a % 400 == 0)):
        d = d + 1
    elif (d ==29 and m==2):
        d = 1
        m = 3
    else:
      d = d + 1
    return d, m, a

def sumardias(d,m,a,n):
  while (n < 0):
    d, m, a = diasiguiente(d, m, a)
    n = n - 1
    #print(n)
    #print(d,m,a)
    #time.sleep(0.05)
  return d,m,a



result =2
while (result != 1):
  print("ingresemos una fecha: _ / _ / _")
  d = int(input("ingrese el dia: "))#29
  print("ingresemos una fecha: dia / _ / _")
  m = int(input("ingrese el mes: "))#2
  print("ingresemos una fecha: dia / mes / _")
  a = int(input("ingrese el año: "))#1956
  print("ingresemos una fecha: dia / mes / año")
  result = verificar_fecha(d,m,a)
  if (result < 0):
    print("la Fecha ingresada es incorrecta")
  if (result > 0):
      print("la Fecha ingresada es correcta")
      print("La fecha es: ",d,"/",m,"/",a,sep="")

# --- el siguiente --- #
d1, m1, a1 = diasiguiente(d, m, a)
print("La fecha de mañana sera: ",d1,"/",m1,"/",a1,sep="")
dias =int(input("Ingrese la cantidad de dias a sumar: "))
#d2, m2, a2 = diasiguiente(d, m, a)
d2, m2, a2 = sumardias(d,m,a,dias)
print("la nueva fecha sera: ",d2,"/",m2,"/",a2,sep="")
