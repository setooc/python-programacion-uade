# Trabajo Práctico 4: Cadenas de caracteres
# 1. Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
# utilizar cadenas auxiliares. Escribir además un programa que permita verificar su
# funcionamiento

def cad_capicua(cad):
	largo = len(cad)
	flag = False
	mitad = largo / 2
	#print(mitad)
	#print(largo)
	if((largo% 2) == 0):
		mitad = int(mitad)
		#print("Reviso valores cadena PAR: \n")
		#print("Valor A: ", cad[:mitad-1:-1])
		#print("Valor B: ", cad[:mitad:])
		if(cad[:mitad:] == cad[:mitad-1:-1]):
			flag = True

	else:#(largo/2) + 0.5
		mitad = int(mitad + 0.5)
		#print("Reviso valores cadena IMPAR: \n")
		#print("Valor A: ",cad[:mitad-1:])
		#print("Valor B: ",cad[:mitad-1:-1])
		if(cad[:mitad-1:] == cad[:mitad-1:-1]):
			flag = True

	return flag

cad = str(input("Inserte una cadena de caracteres: \n"))
valor = cad_capicua(cad)
if (valor):
	print("La cadena ingresada es capicúa")
else:
	print("La cadena ingresada no es capicua")
