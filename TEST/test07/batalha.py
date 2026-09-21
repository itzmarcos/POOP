from abc import abstractmethod
import random
class Personagem():
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca = 100):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f'{self.nome}({self.vida}) atacou {alvo.nome}({self.vida}) com um {golpe} de força {forca}')
            alvo.receber_dano(forca)
        else:
            print(f'O ataque {self.nome} -> {alvo.nome} não pode acontecer.')
        
    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f'{self.nome} recebeu dano de {fator}!')

    @abstractmethod
    def curar():
        pass

class Knight(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Exori", "Exori mas", "Exori gran ico"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'O {self.nome} usou exura med ico e curo-se {fator} de vida')

class Sorcerer(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Exevo gran mas flam", "Vis hur", "Flam hur"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f'O {self.nome} usou exura vita e curo-se {fator} de vida')