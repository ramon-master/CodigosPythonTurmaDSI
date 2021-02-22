def calculaImposto(sal,imposto = 20):
    imposto = imposto/100 #calcular a porcentagem do valor
    novoSalario = sal - (sal*imposto)
    
    return novoSalario

salario = float(input("Informe seu salário: "))
#desconto desconto = float(input("Qual o valor da porcentagem de imposto:"))

print(f"Seu salario liquido é R${calculaImposto(salario)}")