while True:
    valor = int(input("Informe um valor qualquer: "))

    if valor < 0:
        break
    if valor > 100:
        print("LIMITE EXCEDIDIO")
    elif valor > 10:
        print(f"O Quadrado de valor {valor} é {valor **2}")
    elif valor > 5:
        print(f"O cubo de {valor} é {valor**3}")