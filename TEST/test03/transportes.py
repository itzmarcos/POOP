from abc import abstractmethod

class Transporte():
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    
    @abstractmethod
    def calc_frete():
        pass

class Moto(Transporte):
    fator = 0.50
    def __init__(self, distancia):
        super().__init__(distancia)
        self.frete = Moto.fator * self.distancia
    
    def calc_frete(self):
        return f'{self.frete:.2f}'
    


class Caminhao(Transporte):
    fator = 1.20
    def __init__(self, distancia):
        super().__init__(distancia)
        self.frete = Caminhao.fator * self.distancia
        

    def calc_frete(self):
        if self.distancia < 50:
            return f'Raio minimo de 50km'
        else:
            return f'{self.frete:.2f}'

class Drone(Transporte):
    fator = 9.50
    def __init__(self, distancia):
        super().__init__(distancia)
        self.frete = Drone.fator * self.distancia
        

    def calc_frete(self):
        if self.distancia > 10:
            return f'Raio maximo de 10km'
        else:
            return f'{self.frete:.2f}'
        
