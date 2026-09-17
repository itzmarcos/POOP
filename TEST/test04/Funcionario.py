from abc import abstractmethod

class Funcionario():
    sal_min = 1612
    inss = 7.5

    def __init__(self, nome = None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0
        

    @abstractmethod    
    def calc_sal(self):
        pass

    def analisar_sal(self):
        base = self.salario / Funcionario.sal_min
        print(f'O salário de {self.nome} é de R${self.salario:.2f} e corresponde a {base:.1f} salarios minimos')

class Horista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, qts_hora = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qts_hora = qts_hora
        self.sal_bruto = self.valor_hora * self.qts_hora

    def calcular_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)

class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto = Funcionario.sal_min):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calcular_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)