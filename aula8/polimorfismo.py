class Pessoa:
    def __init__(self,nome):
        self.nome = nome
        self.__cpf = ""

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,valor):
        if len(valor) != 11 :
            print("O CPF precisa ter 11 numeros e tem que ser somente numeros")
        elif valor.isnumeric():
            self.__cpf = valor
        else:
            print("Insira apenas numeros")

    def exibirDados(self):
        print(f"Nome:{self.nome}")
        #print(f"CPF:{self.__cpf}")

class Aluno(Pessoa):
    def __init__(self,nome,matricula,curso="nenhum"):
        super().__init__ (nome) #parãmetro self só é preciso se nao for usar super()
        self.matricula = matricula
        self.curso = curso
    
    def exibirDados(self):
        super().exibirDados()
        print(f"Matricula:{self.matricula}")
        print(f"Curso:{self.curso}")

class Professor(Pessoa):
    def __init__(self,nome,salario,ch):
        super().__init__(nome)
        self.salario = salario
        self.ch = ch

    def exibirDados(self):
        super().exibirDados()
        print(f"Salario: R${self.salario}")
        print(f"Carga Horaria: R${self.ch}")