meses=int(input("ingrese la edad en meses del bebe "))
libras=int(input("ingrese el peso del bebe en libras "))
libras=libras+10
meses=meses*10
dosis=libras/meses*8
print("la dosis a aplicar son ",dosis," milimetros cubicos")