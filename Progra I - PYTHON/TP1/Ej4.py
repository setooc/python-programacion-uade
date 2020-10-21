# Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo
# dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema
# de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar
# una función que reciba como parámetro la cantidad de viajes realizados en un
# determinado mes y devuelva el total gastado en viajes. Realizar también un programa
# para verificar el comportamiento de la función.

# Cantidad de viajes Valor del pasaje
# 1 a 20 Averiguar valor actualizado = $10
# 21 a 30 20% de descuento sobre tarifa máxima
# 31 a 40 30% de descuento sobre tarifa máxima
# Más de 40 40% de descuento sobre tarifa máxima

def calcular_gastos(v):
    suma = 0
    tarifa = 10
    if (v < 21):
        suma = v * 10
    if (v > 20 and v < 31):
        suma = v * (10/1.2)
    if (v > 30 and v < 41):
        suma = v * (10/1.3)
    if (v>40):
        suma = v * (10/1.4)
    return suma
    
print("Total de gastos en subte")
viajes = int(input("Ingrese total de viajes del mes: "))
print("El gasto total es: $", calcular_gastos(viajes))
