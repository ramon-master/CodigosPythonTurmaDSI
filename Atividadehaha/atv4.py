lista = []

def listaNomes():
    while True:
        lista.append(str(input("Informe um nome: ")).title())

        op = str(input("deseja continuar s/n: ")).lower()

        if op == "n":
            break
def excluiNomes():
    for indice,nomes in enumerate(lista):
        print(f"{indice}: {nomes}")

    pos = int(input("Qual a posicao da pessoa que voce deseja excluir ? "))

    print(" Excluido com sucesso!\n ")
    
    lista.pop(pos)

while True:
    print("1. Inserir nomes: ")
    print("2. Excluir nomes: ")
    print("3. Sair")

    op = int(input("Qual sua opcao: "))
    if op == 1:
        listaNomes()
    elif op ==2:
        excluiNomes()
        print(lista)
    elif op == 3:
        break