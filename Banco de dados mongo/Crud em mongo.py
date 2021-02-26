from pymongo import MongoClient
# estabelecendo a conexao
cliente = MongoClient('localhost',27017)

banco = cliente.santander# criando um banco

colecao = banco.clientes# criando collections

while True:
    print(f"{' Menu ':^40}")
    op = int(input('''
        1. Inserir dados
        2. Exibir dados
        3. Excluir dados
        4. Sair

        qual sua escolha :'''))
    if op == 1:
        cpf = int(input("Informe o seu cpf(somente numeros):"))
        nome = str(input("Informe o seu nome: ")).title()
        sexo = str(input("Informe o seu sexo:(m/f ): ")).lower()
        sal = float(input("Informe o seu salario :"))
        end = str(input("Informe o seu endereço :"))

        #inserindo dados na collection
        colecao.insert_one({
            'cpf':cpf,
            'nome':f'{nome}',
            'sexo':f'{sexo}',
            'salario':sal,
            'endereço':f'{end}'
        })
        print("\ndados inseridos com sucesso\n")


    elif op == 2:
        print(f"{' Exibindo os dados ':^40}")
        for item in colecao.find():
            print(f"{item['nome']}, possui salario de {item['salario']} e mora no endereço{item['endereço']} com cpf={item['cpf']}")
        print("-"*40)
    elif op == 3:
        escolha = int(input("Qual o cpf do cliente que deseja excluir:"))
        resultado = colecao.delete_one({
            'cpf': escolha 
        })
        print("Clientes excluidos: ", resultado.deleted_count)
        # contando quantos itens foram excluidos

    elif op == 4:
        break