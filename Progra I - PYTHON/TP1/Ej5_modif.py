# Un comercio de electrodomésticos necesita para su línea de cajas un programa que
# le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
# dos números enteros, correspondientes al total de la compra y al dinero recibido.
# Informar cuántos billetes de cada denominación deben ser entregados al cliente como vuelto,
# de tal forma que se minimice la cantidad de billetes.
# Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1.
# Emitir un mensaje de error si el dinero recibido fuera insuficiente.
# Ejemplo: Si la compra es de $317 y se abona con $500,
# el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete de $20,
# 1 billete de $10 y 3 billetes de $1


def calcula_vuelto(compra, pago):
    a = 0# 500
    b = 0# 100
    c = 0# 50
    d = 0# 20
    e = 0# 10
    f = 0# 5
    g = 0# 1
    vuelto = pago - compra
    print("El vuelto sera: ", vuelto)
    print()

    if(vuelto < 0):
        print("Error en el pago")
        return 0, 0, 0, 0, 0, 0
    while (vuelto != 0):
        if(vuelto >= 500):
            a = a + 1
            vuelto = vuelto - 500
        else:
            if(vuelto >= 100):
                b = b + 1
                vuelto = vuelto - 100
            else:
                if (vuelto >= 50):
                    c = c + 1
                    vuelto = vuelto - 50
                else:
                    if (vuelto >= 20):
                        d = d + 1
                        vuelto = vuelto - 20
                    else:
                        if (vuelto >= 10):
                            e = e + 1
                            vuelto = vuelto - 10
                        else:
                            if(vuelto >= 5):
                                f = f + 1
                                vuelto = vuelto - 5
                            else:
                                if (vuelto >= 1):
                                    g = g + 1
                                    vuelto = vuelto - 1

    return a, b, c, d, e, f, g

while(True):
    print()
    print("--- Sistemas de cajas ---")
    print()
    compra = int(input("Ingrese monto total de la compra: "))
    pago = 0
    while (pago < compra):
        pago = int(input("Ingrese monto abonado por cliente: "))
        if (pago < compra):
            print("--- Error el pago es insuficiente ---")
    a, b,c,d,e,f,g = calcula_vuelto(compra, pago)
    print()
    print(a, "billetes de 500")
    print(b, "billetes de 100")
    print(c, "billetes de 50")
    print(d, "billetes de 20")
    print(e, "billetes de 10")
    print(f, "billetes de 5")
    print(g, "billetes de 1")
