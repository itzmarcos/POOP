from abc import abstractmethod

class BebidaQuente:
    def __init__(self):
        pass      

    def preparar(self):
        print('------ Iniciando o Preparo ------')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print('--------- Bebida Pronta ---------')

    def ferver_agua(self):
        print('1. Fervendo água a 100 graus Celsius')
  
    @abstractmethod
    def misturar():
        pass

    @abstractmethod
    def servir():
        pass

class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print('2. Passando água pressurizada pelo o pó de café moído.')

    def servir(self):
        print('3. Servindo em xicara pequena.')
    
class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print('2. Mergulhando o sachê de ervas na água.')
    
    def servir(self):
        print('3. Servindo na caneca de porcelana com limão.')

class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        print('2. Passando vapor pressurizado pelo o bico do leite.')

    def servir(self):
        print('3. Servindo na caneca grande, já com café.')