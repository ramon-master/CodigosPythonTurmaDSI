temp= []

mes = ("Janeiro,Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")
media = 0

for cont in range (1,13):
    temp.append(float(input(f"Informe a temperatura do mes {cont}:")))

    media= sum(temp)/cont
print(f"A media anual de temperatura foi {media:.2f}\n")
for indice,cont in enumerate(temp):
    if cont > media:
        print(f"{mes[indice]:.<10}:{cont}")