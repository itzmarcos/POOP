from abc import abstractmethod
class Animal:
    def __init__(self, nome):
        self.nome = nome
    @abstractmethod
    def som(self):
        pass

class Gato(Animal):
    def som(self):
        return f'{self.nome}: MIAUU MIAUU '

class Cachorro(Animal):
    def som(self):
        return f'{self.nome}: AUU AUU'

class Galinha(Animal):
    def som(self):
        return f'{self.nome}: PIUU PIUU'