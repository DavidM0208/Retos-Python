from random import randint
repeat="SI"
repetir="si"
juego=0
saldo=0


while repeat=="si" or repeat=="SI":
    plata=int(input("Ingrese el saldo que desea recargar "))
    saldo=saldo+plata
    print("Su saldo global es de ",saldo)
    if saldo>=0:
        repeat=input("Si desea ingresar mas dinero escriba si, de lo contrario escriba no \n ")
    else:
        break
apuesta=int(input("Ingrese el valor que desea apostar \n"))
while repetir=="si" or repetir=="SI":
    moneda=randint(1,2)
    eleccion=int(input("Digite 1 para escoger cara o 2 para escoger sello "))
    if moneda==1 and eleccion==1:
        saldo=saldo+apuesta
        juego=juego+1
        print("Salio cara, usted escogio cara, Ganaste!!, debes duplicar tu apuesta")
    elif moneda==1 and eleccion==2:
        saldo=saldo-apuesta
        juego=juego+1
        print("Salio cara, usted escogio sello, Perdiste!!")
        if saldo>0:
            print("Puede seguir jugando")
        elif saldo<0:
            print("Saldo insuficiente")
        else:
            break
    elif moneda==2 and eleccion==2:
        saldo=saldo+apuesta
        juego=juego+1
        print("Salio sello, usted escogio sello, Ganaste!!, debes duplicar tu apuesta")
    elif moneda==2 and eleccion==1:
        saldo=saldo-apuesta
        juego=juego+1
        print("Salio sello, usted escogio cara, Perdiste!!")
        if saldo>0:
            print("Puede seguir jugando")
        elif saldo<0:
            print("Saldo insuficiente")
        else:
            break
    elif eleccion==1 or eleccion==2:
        print("Digitaste una opcion incorrecta")
    else:
        print("Datos incorrectos")
    print(f"Su saldo actual es ",saldo)
    repetir=input(f"Si quiere jugar de nuevo escriba si o de lo contrario escriba no \n")
    if saldo<=0:
        plata=int(input("Ingrese el saldo que desea recargar "))
    elif repetir=="si" or repetir=="SI":
        apuesta=int(input("Ingrese el valor que desea apostar \n"))
    else:
        break
print("El número de veces que usted jugo fue ",juego," el dinero acumulado fue",saldo)