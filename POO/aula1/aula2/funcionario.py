class Funcionario:
    def ___init___(self,nome,cargo,salario=1100):
        self.nome = nome
        self.funcao = cargo
        self.sal = salario 


    def relatorio(self):
        print(f"Nome: {self.nome}, Cargo: {self.funcao}, Salario: {self.sal}")

