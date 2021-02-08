from random import randint
aleatorio = []
for con in range(1,21):
    aleatorio.append(randint(1,900))

for cont in range(3,0,-1):
    print(f"Voce tem {cont} chances para descobrir um dos valores da lista ")
    op = int(input("Informe um valor: "))

    if op in aleatorio:
        print(f"{'PARABENS':*^40}")
        print("vOCE CONSEGUIU ENCONTRAR O VALOR")

        break
    else:
        print("Eita, ainda nao é esse valor, voce consegue, ;)")
        print(aleatorio,"\n\n")