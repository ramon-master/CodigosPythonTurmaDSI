
m2 = 850 #valor referente ao metro quadrado 

base = float(input("qual a largura (base) do terreno? "))
altura = float(input( " Qual o comprimento (altura) do terreno?"))

area = base * altura

custo = area * m2
print(" Voce ira pagar um total de R${} para construir.\n\n".format(custo))