from random import randint


election=int(input("Oprima 1 para ingresar el valor de su compra o oprima 2 para ingresar la cantidad de productos \n"))
if election==1:
    compra=int(input("Ingrese el valor de su compra \n"))
else:
    numeroproductos=int(input("Ingrese la cantidad de productos \n"))
    valorproducto=10000
    compra=numeroproductos*valorproducto

descuento=randint(1,4)
total=compra
if compra>=50000:
    print("El cliente puede participar para beneficio del descuento por su compra")
    if descuento==1:
        calculo=compra*0.10
        total=compra-calculo
        print("Salio bolita roja, su descuento es del 10%, su total a pagar es" , total)
    elif descuento==2:
        calculo=compra*0.30
        total=compra-calculo
        print("Salio bolita azul, su descuento es del 30%, su total a pagar es" , total)
    elif descuento==3:
        calculo=compra*0.50
        total=compra-calculo
        print("Salio bolita azul, su descuento es del 50%, su total a pagar es" , total)
    elif descuento==4:
        print("Salion bolita blanca, te llevas totalmente gratis tu compra")
    else:
        print(f"El juego escogio {descuento}")
else:
    print("El cliente no puede participar para participar den beneficio de descueto de su compra, su total a pagar es ",compra)
if descuento==1 or descuento==2 or descuento==3:
    valorrecibido=int(input("Ingrese el valor con el que desea pagar "))
    cambio=valorrecibido-total
    print("Su compra fue de ",total,", realizo el pago con ",valorrecibido," su cambio es de ",cambio)
else:
    descuento==4
    print("¡¡GANASTE!!")