while True:
    try:
        salario = float(input("Informe seu salario"))
    except Exception as erro:
        print("Informe um valor decimal correto, o erro foi {erro.__class__}")
    else:
        break
    
    
print(f"Seu salario é: R${salario}")