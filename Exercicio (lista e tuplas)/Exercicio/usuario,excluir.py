from os import system
from time import sleep

contato = {}
listacontato = []

while True:
    system("cls")
    print("="*40)
    print(f"{'Agenda'}")
    print("="*40)

    for itens in listacontato:
        for chave, valor in itens.items():
            print(f"{chave}:{valor}")

    print("1. Inserir um contato ")
    print("2. Excluir um contato ")
    print("3. Sair")
    op = int(input("Qual sua escolha? "))

    if op == 3:
        break
    elif op == 1:
        nome = str(input("Informe o nome do contato: "))
        fone = int(input("Informe somente o numero do contato(98xxxxxxxx)"))

        contato[nome] = fone# a chave sera o nome do contato e o valor será seu telefone

        listacontato.append(contato.copy())

        contato.clear()
    elif op ==2:
        escolha = str(input("Informe o nome da pessoa que deseja excluir:")).title()
        for itens in listacontato:
            if escolha in itens.keys():
                itens.pop(escolha)
            else:
                print("Esse contato nao existe, tente de novo")
                sleep(1)
print("="*40)
