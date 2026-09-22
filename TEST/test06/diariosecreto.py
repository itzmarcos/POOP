class Diario():
    def __init__(self, senhachave = 'Admin'):
        self.__segredos = []
        self.__senha = senhachave.strip()
        
    @property
    def senha(self):
        raise PermissionError ('Senha Invalida')
    
    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())
                       
    def ler(self, senha = None):
        if senha != self.__senha:
            raise PermissionError('Senha Invalida!')
        else:
            print(f'Diario Liberado!')
            for segredo in self.__segredos:
                print(f'- {segredo}')