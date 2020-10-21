# Desarrollar cada una de las siguientes funciones y escribir un programa que permita
# verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
# a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
# teclado.
# b. Ordenar en forma ascendente cada una de las filas de la matriz.
# c. Intercambiar dos filas, cuyos números se reciben como parámetro.
# d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
# e. Intercambiar una fila por una columna, cuyos números se reciben como parámetro.
# f. Transponer la matriz sobre si misma. (intercambiar cada elemento A ij por Aji)
# g. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
# parámetro.
# h. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número
# se recibe como parámetro.
# i. Determinar si la matriz es simétrica con respecto a su diagonal principal.
# j. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
# k. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo una lista con los números de las mismas.

def crear_matriz(matriz,dim):
    filas = columnas = dim
    for i in range(filas):
        matriz.append([0] * columnas)

def cargar_matriz(matriz):
    columnas = filas = len(matriz)
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = int(input("Ingresar los datos de la matriz [{}][{}] = ".format(i,j)))


def mostrar_matriz(matriz):
    filas=columnas=len(matriz)
    for i in range(filas):
        for j in range(columnas):
            print("%3d" %matriz[i][j], end="")
        print()

def ordenar_fila(matriz):
    filas=len(matriz)
    for i in range(filas):
        matriz[i].sort()

def intercambiar_fila(f1,f2,matriz):
    temp = []
    temp.append(matriz[f1])
    matriz[f1] = matriz[f2]
    matriz[f2] = temp[0]

def intercambiar_colum(c1,c2,matriz):
    aux=0
    columna=len(matriz)
    for i in range(columna):
        aux = matriz[i][c1]
        matriz[i][c1] = matriz[i][c2]
        matriz[i][c2] = aux

def intercambiar_fila_colum(f1,c1,matriz):
    aux = 0
    largo = len(matriz)
    lista_fila_a_colum = list(matriz[f1])
    lista_columna_a_fila = []
    print("Fila a columna: " ,lista_fila_a_colum)
    for c in range(largo):
        lista_columna_a_fila.append(matriz[c][c1])
    print("Columna a fila: " ,lista_columna_a_fila)
    for i in range(largo):
        matriz[f1][i] = lista_columna_a_fila[i]
    for j in range(largo):
        matriz[j][c1] = lista_fila_a_colum[j]


def matriz_traspuesta(matriz):
    largo = len(matriz)
    for f in range(largo):
        for c in range(largo):
            if (f!=c and f<c):
                aux = matriz[c][f]
            #print("aux = ",aux)
                matriz[c][f] = matriz[f][c]
            #print("matriz[f][c]",matriz[f][c])
                matriz[f][c] = aux
            #print("matriz[c][f]",matriz[c][f])

def fila_promedio(fprom, matriz):
    largo = len(matriz)
    suma = 0
    for f in range(largo):
        suma = suma + matriz[fprom][f]
    promedio = float(suma / (f+1))
    return promedio

def columna_num_impar(matriz, impar):
    largo = len(matriz)
    count = 0
    for c in range(largo):
        if ((matriz[c][impar] %2) != 0):
            count = count + 1
    count = count / largo
    return count

def matriz_simetrica1(matriz):
    largo = len(matriz)
    for f in range(largo):
        for c in range(largo):
            if (f!=c):
                if (matriz[f][c] != matriz[c][f]):
                    return -1
    return 1

def matriz_simetrica2(matriz):
    largo = len(matriz)
    for f in range(largo):
        for c in range(largo):
            if (f!=c):
                if (matriz[f][c] != matriz[c][f]):
                    return -1
    return 1

def matriz_simetrica2(matriz):
    largo = len(matriz)
    for f in range(largo):
        for c in range(largo):
            if ((f+c) != (largo + 1)):
                if (matriz[f][c] != matriz[c][f]):
                    return -1
    return 1

def columna_capicua(matriz):
    largo = len(matriz)
    mitad = largo / 2
    for i in range(largo):
        for j in range(largo):
            if (j < mitad):
                if (matriz[i][j] != matriz[i][(largo-1) - j]):
                    return -1
    return 1
            
matriz = []
print("Sistema de Matrices")
dim = int(input("Ingrese la dimension de la matriz: "))
crear_matriz(matriz,dim)
mostrar_matriz(matriz)

# --- a) --- #
cargar_matriz(matriz)
mostrar_matriz(matriz)
print("Ordenamos las filas por orden ascendente...")

# --- b) --- #
ordenar_fila(matriz)
print("La matriz resulta: ")
mostrar_matriz(matriz)

# --- c) --- #
print()
print("Intercambiamos filas...")
print()
f1 = int(input("Ingrese la primer fila que quiere intercambiar: ")) -1
f2 = int(input("Ingrese la otra fila que quiere intercambiar: ")) -1
intercambiar_fila(f1,f2,matriz)
print("La matriz resulta: ")
mostrar_matriz(matriz)

# --- d) --- #
print()
print("Intercambiamos Columnas...")
print()
c1 = int(input("Ingrese la primer columna que quiere intercambiar: ")) -1
c2 = int(input("Ingrese la otra columna que quiere intercambiar: ")) -1 
intercambiar_colum(c1,c2,matriz)
print("La matriz resulta: ")
mostrar_matriz(matriz)

# --- e) --- #
print()
print("Intercambiamos Fila por Columna...")
print()
f1 = int(input("Ingrese la primer fila que quiere intercambiar: ")) -1 
c1 = int(input("Ingrese la columna que quiere intercambiar: ")) -1 
intercambiar_fila_colum(f1,c1,matriz)
print("La matriz resulta: ")
mostrar_matriz(matriz)

# --- f) --- #
print()
print("Matriz Traspuesta...")
print()
matriz_traspuesta(matriz)
print("La matriz resulta: ")
mostrar_matriz(matriz)

# --- g) --- #
fprom = int(input("Ingrese la fila que desea saber su promedio: ")) -1
prom = fila_promedio(fprom, matriz)
print("El promedio de la fila %d es %.2f" %(fprom+1,prom))
print()
impar=int(input("Ingrese la columna para saber que porcentaje de numeros son impares: ")) -1
porciento = columna_num_impar(matriz, impar)
print("El porcentaje de numeros impares en la columna %d es de %%%.2f" %(impar+1,porciento*100))

# --- i) --- #
print("Revisamos si la matriz es simetrica respecto de su diagonal principal")
valor = matriz_simetrica1(matriz)
if (valor > 0):
    print("La matriz es simetrica!!")
else:
    print("La matriz NO es simetrica")

# --- j) --- #
print("Revisamos si la matriz es simetrica respecto de su diagonal secundaria")
valor = matriz_simetrica2(matriz)
if (valor > 0):
    print("La matriz es simetrica!!")
else:
    print("La matriz NO es simetrica")

# --- k) --- #
print("Revisamos si tenemos columnas capicuas")
valor = columna_capicua(matriz)
if (valor > 0):
    print("La matriz tiene columnas capicua")
else:
    print("La matriz NO tiene columnas capicua")
