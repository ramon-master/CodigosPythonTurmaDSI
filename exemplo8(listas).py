pessoas = ["Fabio","Carlos","Regina","Vanusa"]

print(type(pessoas))

print(pessoas)

pessoas [1] = "Sergio"
# Adicionado elementos
pessoas.append("Sarah")# adicionei no final
pessoas.insert(2,"Flavio")# adiciona em qualquer lugar

for chave, valor in enumerate(pessoas):
    print(f"{chave:.<5}{valor}")

#removendo elementos
pessoas.pop()#remove o ultimo elemento
pessoas.pop(1)
pessoas.remove("Flavio")
    
print(pessoas)

#copiando listas
pessoasBkp = pessoas
pessoasBkp.append("Jeronimo")
print("\n\n",pessoas)
print(pessoasBkp,"\n\n")



pessoas.clear()# limpa a lista
#del(pessoas) -> excluir a variável lista
print(pessoas,"\n\n")
