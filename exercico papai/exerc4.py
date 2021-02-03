from os import system
soma = 0
for con in range(1,11):
    idade = int(input("Informe a idade da pessoa {cont}"))

    soma += idade

    system("cls")
media = soma / cont
if media <= 25:
    print("A turma é jovem")
elif media >25 and media <=60:
    print("A turma é adulta")
elif media > 60:
    print("A turma é idosa")

    print("\n\n")