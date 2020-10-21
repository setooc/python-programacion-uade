import msvcrt
def calcula_max (a,b,c):
	if( a > b ):
		if( a > c ):
			return a
	if( b > a ):
		if( b > c ):
			return b
	if( c > a ):
		if( c > b ):
			return c
	else:
		return -1
#if __name__ == '__main__':

a = int(input("ingrese a: "))
b = int(input("ingrese b: "))
c = int(input("ingrese c: "))
max = calcula_max (a,b,c)
print("El numero mas grande es: ", max)
msvcrt.getch() #para pausar la consola
