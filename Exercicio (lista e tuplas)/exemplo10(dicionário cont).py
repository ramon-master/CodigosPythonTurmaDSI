pessoas = {"Nome": "Bruno",
"idade":21,
"Bairro":"Turu"
}


print(pessoas)

print(f"Olá {pessoas['Nome']}, voce tem {pessoas['idade']} e mora no bairro {pessoas['Bairro']}'\n\n")
# print(type(pessoas))

print(pessoas.keys())#exibindo as chaves
print(pessoas.values())# exibindo o conteudo
print(pessoas.items())# exibindo o conteudo

# exibir as chaves 
for chave, valor in pessoas.items():
    print(f"{chave.title()} = {valor}")# title() - deixar 1ª letra em maiusculo

#inserindo mais uma chave e valor
pessoas.update({'sexo':'m'})
print(pessoas)

#pessoas.get()
print("\n\n")

#prencher um lista com dicionarios

lista = []
for cont in range(0,2):
    pessoas["Nome"] = input("Informe seu nome: ")
    pessoas["idade"] = input("Informe seu idade: ")
    pessoas["bairro"] = input("Informe seu bairro: ")
    pessoas["sexo"] = input("Informe seu sexo: ")

    lista.append(pessoas.copy())# copy dicionario dentro de uma lista

print(lista)

print(lista[0]['nome'])# mostrando um item dentro da lista