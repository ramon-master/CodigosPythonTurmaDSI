valores = list()

for cont in range(1,11):
    valores.append(int(input(f"Informe o valor {cont}: ")))

print(valores)

for indice,cont in enumerate (valores):
    if cont % 2==0:
        #valores.remove(cont)
        valores.pop(indice)
print(f"Lista sem os valores pares: {valores}\n\n")
