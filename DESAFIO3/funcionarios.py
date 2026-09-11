from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome
        self._salario = None

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        self._salario = valor

    def calcular_bonus():
        pass

class Gerente(Funcionario):
#BONUS 15%
    pass

class Designer(Funcionario):
#BONUS 8%
    pass

class Desenvolvedor(Funcionario):
#BONUS 10%
    pass 