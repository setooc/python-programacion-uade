def dibujar (f):
    for i in range(1,f+1):
        dibujo=str("**")
        for j in range(1,i+1):
            print(dibujo,end="")
        print()

filas = int(input("ingrese un numero de filas: "))
dibujar(filas)
