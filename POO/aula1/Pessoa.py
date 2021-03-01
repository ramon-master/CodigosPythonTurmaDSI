from datetime import date

class Pessoa:
    #atributo
    Nome = "José"
    idade = 45
    altura = 1.65

    # método 
    def falar(self, texto):
        print(texto)

    def pensar(self):
        print()

    def deitar(self):
        pass
    def calculaAno(self,idade):
        anoAtual = date.today().year
        print(f"Voce nasceu no ano de {anoAtual - idade}")
