import time
import os


totalPessoas = int(input("Serao dadas boas vindas para quantas pessoas ?"))

#CONTADORES
homens = 0
mulheres = 0

for cont in range(1,totalPessoas+1):
    nome = input("Qual o seu nome ?")
    sexo = input("Qual o seu sexo ? m/f ")

    if sexo == "m":
        print(f"Bem vindo Sr.{nome} ")
        homens +=1
    else:
        print(f"bem vindo Sr. {nome}")
        mulheres += 1

    time.sleep(5)# espere 5 segundo
    os.system("cls")# limpa tela