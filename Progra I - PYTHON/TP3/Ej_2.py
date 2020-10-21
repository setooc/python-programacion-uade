# Para cada una de las siguientes matrices, desarrollar una función que la genere y
# escribir un programa que invoque a cada una de ellas y muestre por pantalla la
# matriz obtenida. El tamaño de las matrices debe establecerse como N x N, y las
# y funciones deben servir aunque este valor se modifique.

def generar_matriz(matriz,dim):
	filas = columnas = dim # como es una matriz NXN, filas = columnas
	for i in range(filas):
		matriz.append([0] * filas)

def mostrar_matriz(matriz):
	largo = len(matriz)
	for i in range(largo): # filas
		for j in range(largo): # columnas
			print("%3d" %matriz[i][j], end="")
		print()

def generar_matriz_tipo2(matriz):
	largo = len(matriz)
	for i in range(largo): # filas
		for j in range(largo): # columnas
			if (i==j):
				matriz[i][j]=1
				if (i!=0):
					matriz[i][j]=matriz[i-1][j-1] + 2 

def generar_matriz_tipo3(matriz):
	largo = len(matriz)
	for i in range(largo): # filas
		for j in range(largo): # columnas
			if ( (i+j) == (largo-1)):
				matriz[i][j] = 3**((largo-1) - i)
	
def generar_matriz_tipo4(matriz):
	largo = len(matriz)
	for i in range(largo): # filas
		for j in range(largo): # columnas
			if (i==j or i>j):
				matriz[i][j] = largo -i

	
def generar_matriz_tipo5(matriz):
	largo = len(matriz)
	numero = 2**largo
	for i in range(largo): # filas
		numero = numero // 2
		for j in range(largo): # columnas
			matriz[i][j] = numero
		
	
def generar_matriz_tipo6(matriz):
	pass
	
def generar_matriz_tipo7(matriz):
	pass

def generar_matriz_tipo8(matriz):
	pass
	
	

# --- Main --- #
matriz= []
print("Tipos de matrices")
print()
dim = int(input("Ingrese la dimension de la matriz: "))
print("Matriz A: ") # -- Todos ceros
generar_matriz(matriz,dim)
mostrar_matriz(matriz)
print()

# --- Matriz B --- #
print("Matriz B: ") # -- Diagonal 1 3 5 7
generar_matriz_tipo2(matriz)
mostrar_matriz(matriz)
print()

# --- Matriz C --- #
print("Matriz C: ") # -- Diagonal 27 9 3 1
generar_matriz_tipo3(matriz)
mostrar_matriz(matriz)
print()

# --- Matriz D --- #
print("Matriz D: ") # -- 
generar_matriz_tipo4(matriz)
mostrar_matriz(matriz)
print()

# --- Matriz E --- #
print("Matriz E: ")
generar_matriz_tipo5(matriz)
mostrar_matriz(matriz)
print()

# --- Matriz F --- #
# print("Matriz F: ")
# generar_matriz_tipo6(matriz)
# mostrar_matriz(matriz)
# print()

# --- Matriz G --- #
# print("Matriz G: ")
# generar_matriz_tipo7(matriz)
# mostrar_matriz(matriz)
# print()

# --- Matriz H --- #
# print("Matriz H: ")
# generar_matriz_tipo8(matriz)
# mostrar_matriz(matriz)
# print()