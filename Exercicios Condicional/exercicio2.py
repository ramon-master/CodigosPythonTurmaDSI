peso = float(input("Informe seu peso: "))
altura = float(input(" Informe sua altura: "))

imc = peso / altura**2

if imc <16 and imc <=17:
    print(" Magreza grave ")
elif imc >17 and imc <=18.5:
    print(" Magreza leve ")
elif imc >18.5 and imc <=25:
    print("Saudavel")
elif imc >25 and imc <=30:
    print("Sobrepeso")
elif imc >30 and imc <=35:
    print("Obesidade grau 1")
elif imc >35 and imc <=40:
    print("Obesidade grau II (severa)")
elif imc > 40:
    print("Obesidade grau III (morbido)")
