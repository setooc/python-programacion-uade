# Segundo Parcial 

#eliminar una palabra ingresada por teclado de un archivo de texto.

#con funcion recursiva ver si un numero es primo.

#Para estudiar Clases

class Socio:

    def __init__(self):
        self.nombre=input("Ingrese el nombre del socio:")
        self.antiguedad=int(input("Ingrese la antiguedad:"))

    def imprimir(self):
        print(self.nombre,"tiene una antiguedad de",self.antiguedad)

    def retornar_antiguedad(self):
        return self.antiguedad


class Club:

    def __init__(self):
        self.socio1=Socio()
        self.socio2=Socio()
        self.socio3=Socio()

    def mayor_antiguedad(self):
        print("Socio con mayor antiguedad")
        if (self.socio1.retornar_antiguedad()>self.socio2.retornar_antiguedad() and
            self.socio1.retornar_antiguedad()>self.socio3.retornar_antiguedad()):
            self.socio1.imprimir()
        else:
            if self.socio2.retornar_antiguedad()>self.socio3.retornar_antiguedad():
                self.socio2.imprimir()
            else:
                self.socio3.imprimir()


# bloque principal

club=Club()
club.mayor_antiguedad()


# Otro ejemplo

class Persona:

    def __init__(self):
        self.nombre=input("Ingrese el nombre:")
        self.edad=int(input("Ingrese la edad:"))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)


class Empleado(Persona):

    def __init__(self):
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo:"))

    def imprimir(self):
        super().imprimir()
        print("Sueldo:",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("El empleado debe pagar impuestos")
        else:
            print("No paga impuestos")


# bloque principal

persona1=Persona()
persona1.imprimir()
print("____________________________")
empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()

# EJemplo del curso

# -*- coding: utf-8 -*-
# Atributo
# funciones que viven dentro del objeto son METODOS
# instancia

class Lamp: #las clases comienzan en mayus

    _LAMPS = [
    'ON',
    'OFF'
    ]
#El metodo init(constructor) es el primer metodo que se va a llamar cuando tenemos una nueva instancia, cuando tengamos mas de una instancia
    def __init__(self, is_turned_on): #Metodo de instancia el "self" y el metodo init es el contructor
        self._is_turned_on = False

    # metodo publico
    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    # metodo publico
    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    # metodo privado
    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

def run(): #va a generar una instancia nueva de la clase
    lamp = Lamp(is_turned_on = False) # Inicializamos una clase

    while True:
        command = str(input('''
        ¿Que debemos hacer?

        [p] - prender
        [a] - apagar
        [s] - Salir

        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break

if __name__ == '__main__':
    run()
