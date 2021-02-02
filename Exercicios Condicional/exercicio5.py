vPermitida = float(input("Qual a velocidade permitida? "))
vMotorista = float(input("Qual a velocidade do motorista? "))

# calcular 20% a mais
vPermitida20 = (vPermitida * 0.2) + vPermitida

#calcular 50% a mais
vPermitida50 = (vPermitida * 0.5) + vPermitida

if vMotorista <= vPermitida:
    print("Tudo certo, nao precisa pagar multa")
elif vMotorista > vPermitida and vMotorista <+ vPermitida20:
    print("Voce cometeu infracao media\aAssim ira pagar R$85.00 e receber 4 pontos carteira")
elif vMotorista > vPermitida20 and vMotorista <+ vPermitida50:
    print("Voce cometeu infracao grave\nAssim ira pagar R$127.00 e receber 5 pontos carteira")
elif vMotorista > vPermitida50:
    print("Voce cometeu infracao gravissima\nAssim ira pagar R$574.00 além de recebr 7 pontos carteira\n Ter carteira apreendida e \nTer o direito de dirirgir suspenso")