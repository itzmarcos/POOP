class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def funcao(self):
        pass


class Aluno(Pessoa):
    def funcao(self):
        return f'{self.nome} tem {self.idade} e é aluno na Escola Sinha Saboia'

class Professor(Pessoa):
    def funcao(self):
        return f'{self.nome} tem {self.idade} e é professor na Escola Sinha Saboia'

class Diretor(Pessoa):
    def funcao(self):
        return f'{self.nome} tem {self.idade} e é Diretor na Escola Sinha Saboia'