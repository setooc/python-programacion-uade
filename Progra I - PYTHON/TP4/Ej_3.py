# 3. Escribir un programa que permita ingresar una cadena de #caracteres y coloque en
# mayúscula la primera letra posterior a un espacio, eliminando # todos los espacios
# que contenga. Imprimir por pantalla la cadena obtenida

def camel_case(frase):
	c = 0
	cad = ""
	value = False
	for c in frase:
		if (value):
			letra = chr(ord(c) - 32)
			c = letra
			value = False
		if(c == " "):
			value = True
		if(value == False):
			cad = cad + c	
	return cad
				

frase = str(input("Ingrese una frase: \n"))
print("Su frase es: ", end="")
print(frase)
print("Convertimos a CamelCase")
cad = camel_case(frase)
print(cad)