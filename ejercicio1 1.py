
X=int(input("ingrese un numero"))#solicita el numero
Es_pri = True #True para confirmar si el numero es primo
if X < 1: # Si el numero es menor que 1 el numomero no es primo se cambia estado a false
    Es_pri = False
else:
    for i in range(2, X):
        if X % i == 0:
            Es_pri = False
            break
if Es_pri:
  print(f"El numero:" , X , "si es primo")
else:
  print(f"El numero:" , X , "no es primo")



