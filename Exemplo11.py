from datetime import date
anoAtual = date.today().year
def divisoria():
    print("-"*50)
    
nome = str(input("Infomre seu nome: "))
divisoria()

idade = int(input("Informe sua idade: "))
divisoria()

print(f"Ola {nome} voce nasceu no ano de : {anoAtual - idade}")
divisoria()
