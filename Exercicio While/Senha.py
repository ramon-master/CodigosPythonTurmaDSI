while True:
    login1 = input("Qual o seu login?")
    senha1 = input("Informe a senha ")

    if login1 != senha1:
        while True:
            login2 = input("Qual o login da pessoa 2? ")
            senha2 = input("Qual a senha da pessoa 2")
            if login2 != login1 and login2 != senha2:
                break
            
            else:
                print("Login e senha iguais ou o login é o mesmo da 1ª pessoa")
        break
    else:
        print("Login e senha iguais\n")

