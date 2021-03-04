num1 = int(input("Informe um valor numerico: "))
num2 = int(input("Informe outro valor numerico: "))

try:
    resultado = num1 / num2
except Exception as erro:
    print(f"Houve algum erro: {erro.__class__}")
else:
    print(f"O resultado é {resultado}")