palabra = input("Digite una frase: ")
vocal = "aeiouAEIOU"
cont = 0
for letra in palabra:
    if letra in vocal:
     cont += 1
print("La veces que se repitieron las vocales son: ",cont," veces")