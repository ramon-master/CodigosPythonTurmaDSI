salario = float(input("Informe o salario :"))
hora = float(input("Informe horas trabalhadas :"))

hora_mes = (hora*24)

print("Ele recebe o salario de R$ {:.2f} por hora :".format(salario/hora_mes))