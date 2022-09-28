from random import randint


yo=randint(1,3)
maquina=randint(1,3)
eleccion=int(input("Digite 1 para escoger piedra, digite 2 para escoger papel, digite 3 para escoger tijera "))

if yo==1 and maquina==2: 
    print("Escoji piedra, la maquina escogio papel. ¡Pierdo!...")
elif yo==1 and maquina==3: 
    print("Escoji piedra, la maquina escogio tijera. ¡Gano!...")
elif yo==2 and maquina==3: 
    print("Escoji papel, la maquina escogio tijera. ¡Pierdo!...")
elif yo==2 and maquina==1: 
    print("Escoji papel, la maquina escogio piedra. ¡Gano!...")
elif yo==3 and maquina==1: 
    print("Escoji tijera, la maquina escogio piedra. ¡Pierdo!...")
elif yo==3 and maquina==2: 
    print("Escoji tijera, la maquina escogio papel. ¡Gano!...")
else:
    print("Ambos sacan lo mismo")