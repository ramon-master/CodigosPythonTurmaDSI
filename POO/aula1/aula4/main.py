from associacao import Celular,Pessoa

smartphone = Celular("Xiaomi, 1500")

p1 = Pessoa("Clotilde" , 45,"Rua 71 vila Cascavel")

print(f"{p1.nome} mora no endereço {p1.endereço} e tem {p1.idade} anos")

p1.celular = smartphone

print(f"{p1.nome} possui um celular da marca {p1.celular.marca}e custou R${p1.celular.valor}")