from abc import ABC, abstractmethod
import locale


class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        self._salario = valor

    @property
    def fsalario(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(self._salario, grouping=True, symbol=True)

    def calcular_bonus():
        pass

    

class Gerente(Funcionario):
#BONUS 15%
    def __str__(self):
        return f'{self.nome} ganha {self.fsalario} e por ser Gerente o bonus é de R$ {self.calcular_bonus():.2f}'

    def calcular_bonus(self):
        return self.salario * 0.15

class Designer(Funcionario):
#BONUS 8%
    def __str__(self):
        return f'{self.nome} ganha {self.fsalario} e por ser Designer o bonus é de R$ {self.calcular_bonus():.2f}'

    def calcular_bonus(self):
        return self.salario * 0.08

class Desenvolvedor(Funcionario):
#BONUS 10%
    def __str__(self):
        return f'{self.nome} ganha {self.fsalario} e por ser Desenvolvedr o bonus é de R$ {self.calcular_bonus():.2f}'

    def calcular_bonus(self):
        return self.salario * 0.10