#while (void != 0):

def draw_triangle(num):
	int_num = int(num)
	void = int_num - 1
	for i in range(void):
		print(" ",end="")
	print("*")
	void = void - 1
	esp = 1
	while (void != 0):
		for i in range(void):
			print(" ",end="")
		print("*",end="")
		for i in range(esp):
			print(" ",end="")
		print("*")
		esp = esp + 2
		void = void - 1
	for i in range((esp+2)):
		print("*",end="")

# --- MAIN --- #
num = 0
while (num % 2 == 0 or num<3):
	num = float (input("Ingresar un numero entero e impar, no menor a 3: \n"))
draw_triangle(num)
