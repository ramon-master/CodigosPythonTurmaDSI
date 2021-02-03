for cont in range(1,11):
    print(cont,"",end="")
    # impedido de quebrar linha

for cont in range (1,21,3):# o 3º parametro é incremento dos valores
    print (cont)

for cont in range(11,0,-1):#decrementando os valores
    print(cont,"-",end="")
print("\n\n")
    print("-"*15,"VALORES PARES","-"*15)
    for cont in range(1,11):
        if cont %2 ==0:
            print(cont,"",end="")
