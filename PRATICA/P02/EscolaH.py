class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
    def funcao(self):
        pass


class Aluno(Pessoa):
    def funcao(self):
        return f'{self.nome} tem {self.idade} anos e é aluno na Escola Sinha Saboia'

class Professor(Pessoa):
    def funcao(self):
        return f'{self.nome} tem {self.idade} anos e é {self.cargo} na Escola Sinha Saboia'

class Diretor(Pessoa):
    def funcao(self):
        return f'{self.nome} tem {self.idade} anos e é {self.cargo} na Escola Sinha Saboia'