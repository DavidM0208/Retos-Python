from random import randint

craps=randint(1,6)
craps2=randint(1,6)
print("Lanza los dados, si sale un par de 1 en los dos dados \n un total de 3 en los dados \n un total de 11 en los dados \n un total de 2 o 12 en los dados \n un total de 7 en los dados, Ganaste!... ")
print(f"Lanzar los dados {craps, craps2}")
if craps==1 and craps2==1:
    print("Si sale par de 1, Ganaste!...")
elif craps==1 and craps2==2 or craps==2 and craps2==1:
    print("Si sale un total de 3, Ganaste!...")
elif craps==6 and craps2==5 or craps==5 and craps2==6:
    print("Si sale un total de 11, Ganaste!...")
elif craps==1 and craps2==1 or craps==6 and craps2==6:
    print("Si sale un total de 2 o 12, Ganaste!...")
elif craps==5 and craps2==2 or craps==2 and craps2==5 or craps==4 and craps2==3 or craps==3 and craps2==4:
    print("Si sale un total de 7, Ganaste!...")
else:
    print("El resultado es diferente, Perdiste!...")