lista = []
for cont in range(20):
    lista.append(cont)

print(lista)

#list comprehension

numeros = [cont**2 for cont in range(10)]
print(numeros)

#utilizar lambda

soma = lambda x,y: + y

print(soma(4,5))
#trabalhando com funcao map()
dobro = list(map(lambda x:x*2,lista))

print(dobro)

#trabalhando com a funcao filter
valores = list(range(20,61))
print(valores)

pares = list(filter(lambda num:num%2==0,valores))

print("Os Numeros pares sao:\n",pares)