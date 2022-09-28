from random import randint

descuento=randint(1,4)
valorfactura=int(input("Ingrese el valor de su compra "))
if valorfactura>=50000:
    print("El cliente puede participar para el descuento")
    valorfactura*0,1
    if descuento==1:
        calculo=valorfactura*0.10
        total=valorfactura-calculo
        print("Salio bolita roja, su descuento es del 10%, su total a pagar es" , total)
    elif descuento==2:
        calculo=valorfactura*0.30
        total=valorfactura-calculo
        print("Salio bolita azul, su descuento es del 30%, su total a pagar es" , total)
    elif descuento==2:
        calculo=valorfactura*0.50
        total=valorfactura-calculo
        print("Salio bolita azul, su descuento es del 50%, su total a pagar es" , total)
    elif descuento==3:
        print("Salion bolita blanca, te llevas totalmente gratis tu compra")
else:
    print("El cliente no puede participar para el descuento")