# 1. Una oficina cuneta con dos cajas fuerte cuyas claves son numericas y de 4 cifras
# Para evitar extraviarlas kas combino fomando un solo numero de 8 digitos, en el que las posiciones impares
# corresponden a una de las cajas y las pares a la otra.
# Desarrollar un programa para ingresar la clave combinada y mostar por pantalla ambos codigo de forma individual.
# por ejemplo se ingresa 15263748 debera mostrarse 1234 y 5678

def separa_clave(key):
    aux = 0
    llave = llave_bkp = key
    lista_numeros_clave = []
    caja_1 = 0
    caja_2 = 0
    count_par = 3
    count_impar = 3
    for i in range(8,0,-1):
        div = (llave % 10**i) // 10**(i-1)
        lista_numeros_clave.append(div)
    for j in range (len(lista_numeros_clave)):
        if (j % 2 == 0):
            aux = lista_numeros_clave[j] * (10**(count_par))
            #print("aux1", aux)
            caja_1 = caja_1 + aux
            count_par = count_par -1
        else:
            aux = lista_numeros_clave[j] * (10**(count_impar))
            #print("aux2", aux)
            caja_2 = caja_2 + aux
            count_impar = count_impar -1
    return caja_1, caja_2

# --- Main --- #
key = 0
while (key<10000000 and key<99999999):
    key = int(input("Ingresar la clave combinada (8 digitos): \n"))
print("numero ingresado %d" %(key))
caja_1, caja_2 = separa_clave(key)
print("La clave de la caja 1 es: ", caja_1)
print("La clave de la caja 2 es: ", caja_2)
