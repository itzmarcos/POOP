class Retangulo():
    def __init__(self, base = 1, altura = 1):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self._altura = altura

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, valor):
        if not isinstance(valor, float) and not (valor, int):
            raise TypeError('Erro')
        if valor < 0:
            raise ValueError('Erro 2')
        else:
            self._base = valor

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, float) and not (valor, int):
            raise TypeError('Erro')
        if valor < 0:
            raise ValueError('Erro 2')
        else:
            self._altura = valor